import CosNaming
import sys

from django.test import TestCase
from raven.contrib.django.raven_compat.models import logging
from corba_client.client import Client

# Create your tests here.

logger = logging.getLogger(__name__)

# orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
# print 'ORB typeOf: ',type(orb)
# print 'ORB list_initial_services: ', orb.list_initial_services()
# # print 'ORB resolve_initial_references: ', orb.resolve_initial_references(orb.id())
# print 'Methods ORB: ', [method for method in dir(orb) if callable(getattr(orb, method))]
# # print 'Attributes ORB: ', vars(orb)

# # # Obtain a reference to the root naming context
# obj = orb.resolve_initial_references("LightSoftNameService")
# print '*******************************************************************'
# rootContext = obj._narrow(CosNaming.NamingContext)
#
# if rootContext is None:
#     print "Failed to narrow the root naming context"
#     sys.exit(1)


class aSAPTestCase(TestCase):
    client = Client(None, "NameService")
    obj = client.get_resolved_object("Local_Context", "my_context", "ASAPIterator_I", "Object")
    print 'getLength: ', obj.getLength()
    client = None
    # logger.debug('ASAPIterator_I.next_n', exc_info=True, extra={'class': 'ASAPIterator_I',
    #                                                             'netxt_n': eo.next_n(10)})
    # logger.debug('ASAPIterator_I.getLength', exc_info=True, extra={'class': 'ASAPIterator_I',
    #                                                                'getLength': eo.getLength()})
    # logger.debug('ASAPIterator_I.destroy')


class callSNCTestCase(TestCase):
    client = Client(None, "NameService")
    obj = client.get_resolved_object("Local_Context", "my_context", "CallAndTopLevelConnectionsIterator_I", "Object")
    print 'getLength: ', obj.getLength()
    client = None
    # logger.debug('ASAPIterator_I.next_n', exc_info=True, extra={'class': 'ASAPIterator_I',
    #                                                             'netxt_n': eo.next_n(10)})
    # logger.debug('ASAPIterator_I.getLength', exc_info=True, extra={'class': 'ASAPIterator_I',
    #                                                                'getLength': eo.getLength()})
    # logger.debug('ASAPIterator_I.destroy')


class commonTestCase(TestCase):
    client = Client(None, "NameService")
    obj = client.get_resolved_object("Local_Context", "my_context", "Common_I", "Object")
    print 'setOwner: ', obj.setOwner()

    # eo.setOwner("lala", "bcand")

    # logger.debug('ASAPIterator_I.next_n', exc_info=True, extra={'class': 'ASAPIterator_I',
    #                                                             'netxt_n': eo.next_n(10)})
    # logger.debug('Common_I.setNativeEMSName', exc_info=True, extra={'class': 'Common_I',
    #                                                                'setNativeEMSName':eo.setNativeEMSName(objectName='objectNmae', nativeEMSName=globaldefs_idl.NamingAttributes_T('NamingAttribute1','bcand',True))})
    # logger.debug('Common_I.setUserLabel', exc_info=True, extra={'class': 'Common_I',
    #                                                             'setNativeEMSName': eo.setNativeEMSName(globaldefs_idl.NamingAttributes_T('NamingAttribute1','bcand',True))})