import sys
import CosNaming
from omniORB import CORBA
from raven.contrib.django.raven_compat.models import logging

from corba_client.IDL import aSAP, callSNC


class Client:

    logger = logging.getLogger(__name__)

    def __init__(self, IP, name_service):
        if IP is None:
            self.orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
            self.initial_ref = self.orb.resolve_initial_references(name_service)
        else:
            self.orb = CORBA.ORB_init()
            self.initial_ref = self.orb.string_to_object("corbaloc::", IP, name_service)#????????


        # print 'ORB list_initial_services: ', orb.list_initial_services()
        # print 'ORB resolve_initial_references: ', orb.resolve_initial_references(orb.id())
        # print 'Methods ORB: ', [method for method in dir(self.orb) if callable(getattr(self.orb, method))]
        # print 'Attributes ORB: ', vars(orb)

        # # Obtain a reference to the root naming context
        print '*******************************************************************'
        self.context = self.initial_ref._narrow(CosNaming.NamingContext)

        if self.context is None:
            print "Failed to narrow the root naming context"
            sys.exit(1)

    def get_resolved_object_by_Stringified(self, ior):

        obj = self.orb.string_to_object(ior)

        eo = obj#._narrow(Ca.)

        if eo is None:
            print "Object reference is not an Example::Echo"
            sys.exit(1)
        return eo

    def get_resolved_object(self, context_name, context_type, object_name, object_type):
        name = [CosNaming.NameComponent(context_name, context_type),
                CosNaming.NameComponent(object_name, object_type)]
        try:
            self.obj = self.context.resolve(name)
            print 'Object', self.obj

        except CosNaming.NamingContext.NotFound, ex:
            self.logger.debug("Name not found")
            sys.exit(1)

        # Narrow the object to an Example::Echo
        print 'Methods obj: ', [method for method in dir(self.obj) if callable(getattr(self.obj, method))]
        eo = self.obj#._narrow(callSNC.CallAndTopLevelConnectionsIterator_I)#aSAP.ASAPIterator_I

        if (eo is None):
            print "Object reference is not an ", object_name
            sys.exit(1)
        print '*******************************************************************'
        return eo

    def release(self):
        self = None