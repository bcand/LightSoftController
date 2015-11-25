import CosNaming
import sys

from django.test import TestCase
from omniORB import CORBA
from raven.contrib.django.raven_compat.models import logging
# Create your tests here.

logger = logging.getLogger(__name__)

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
# print 'ORB typeOf: ',type(orb)
print 'ORB list_initial_services: ', orb.list_initial_services()
# print 'ORB resolve_initial_references: ', orb.resolve_initial_references(orb.id())
# print 'Methods ORB: ', [method for method in dir(orb) if callable(getattr(orb, method))]
# print 'Attributes ORB: ', vars(orb)

# # Obtain a reference to the root naming context
obj = orb.resolve_initial_references("NameService")#LightSoftNameService
print '*******************************************************************'
rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
    print "Failed to narrow the root naming context"
    sys.exit(1)


class aSAPTestCase(TestCase):
    name = [CosNaming.NameComponent("Local_Context", "my_context"),
            CosNaming.NameComponent("aSAP_ASAPIterator_I", "Object")]
    try:
        obj = rootContext.resolve(name)
        print 'Object', obj

    except CosNaming.NamingContext.NotFound, ex:
        logger.debug("Name not found")
        sys.exit(1)

    # Narrow the object to an Example::Echo
    eo = obj#._narrow(aSAP.ASAPIterator_I)
    for attr, value in obj.__dict__.iteritems():
        print "Attribute: " + str(attr or "")
        print "Value: " + str(value or "")
    if (eo is None):
        print "Object reference is not an Example::Echo"
        sys.exit(1)

    print eo.getLength()
    # logger.debug('ASAPIterator_I.next_n', exc_info=True, extra={'class': 'ASAPIterator_I',
    #                                                             'netxt_n': eo.next_n(10)})
    # logger.debug('ASAPIterator_I.getLength', exc_info=True, extra={'class': 'ASAPIterator_I',
    #                                                                'getLength': eo.getLength()})
    # logger.debug('ASAPIterator_I.destroy')


# class commonTestCase(TestCase):
#     name = [CosNaming.NameComponent("Local_Context", "my_context"),
#             CosNaming.NameComponent("common_Common_I", "Object")]
#     try:
#         obj = rootContext.resolve(name)
#         # logger.debug('Object', exc_info=True, extra={'obj': obj})
#
#     except CosNaming.NamingContext.NotFound, ex:
#         logger.debug("Name not found")
#         sys.exit(1)
#
#     # Narrow the object to an Example::Echo
#     eo = obj#._narrow(common.Common_I)
#
#     if (eo is None):
#         print "Object reference is not an Common_I_i"
#         sys.exit(1)
#
#     # for attr, value in obj.__dict__.iteritems():
#     #     print "Attribute: " + str(attr or "")
#     #     print "Value: " + str(value or "")
#
#     print 'Look in the server'
#     # print 'Capatibilities: ', eo.getCapabilities()
#     eo.setOwner("lala", "bcand")
#     # logger.debug('ASAPIterator_I.next_n', exc_info=True, extra={'class': 'ASAPIterator_I',
#     #                                                             'netxt_n': eo.next_n(10)})
#     # logger.debug('Common_I.setNativeEMSName', exc_info=True, extra={'class': 'Common_I',
#     #                                                                'setNativeEMSName':eo.setNativeEMSName(objectName='objectNmae', nativeEMSName=globaldefs_idl.NamingAttributes_T('NamingAttribute1','bcand',True))})
#     # logger.debug('Common_I.setUserLabel', exc_info=True, extra={'class': 'Common_I',
#     #                                                             'setNativeEMSName': eo.setNativeEMSName(globaldefs_idl.NamingAttributes_T('NamingAttribute1','bcand',True))})