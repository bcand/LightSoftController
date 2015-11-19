import CosNaming
import sys
from django.test import TestCase
from omniORB import CORBA
from raven.contrib.django.raven_compat.models import  logging
# from corba_client.IDL import aSAP_idl, globaldefs_idl, common_idl, globaldefs

# Create your tests here.

logger = logging.getLogger(__name__)

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
print 'ORB typeOf: ',type(orb)
print 'ORB list_initial_services: ', orb.list_initial_services()
print 'Methods ORB: ', [method for method in dir(orb) if callable(getattr(orb, method))]

# # Obtain a reference to the root naming context
obj = orb.resolve_initial_references("LightSoftNameService")
print '*******************************************************************'
print 'NameService: ', orb.object_to_string(obj)
print 'NameService typeOf: ',type(obj)
print 'Methods NameService: ', [method for method in dir(obj) if callable(getattr(obj, method))]
# for s in list:
#     print s

rootContext = obj._narrow(CosNaming.NamingContext)
# rootContext = CosNaming.NamingContextExt._narrow(obj)
print 'RootContext: %s' % (orb.object_to_string(rootContext))

if rootContext is None:
    print "Failed to narrow the root naming context"
    sys.exit(1)


class aSAPTestCase(TestCase):

    # Resolve the name "test.my_context/ExampleEcho.Object"
    name = [CosNaming.NameComponent("1stLocalNameContext", "1st_context"),
            CosNaming.NameComponent("aSAP_ASAPIterator_I", "Object")]
    try:
        obj = rootContext.resolve(name)
        logger.debug('Object', exc_info=True, extra={'obj': obj})
        print 'aSAPTestCase typeOf: ',type(obj)
        print 'aSAPTestCase _get_interface: ', obj._get_interface()
        print 'Methods aSAPTestCase: ', [method for method in dir(obj) if callable(getattr(obj, method))]

    except CosNaming.NamingContext.NotFound, ex:
        logger.debug("Name not found")
        sys.exit(1)

    # Narrow the object to an Example::Echo
    eo = obj#._narrow(aSAP_idl.ASAPIterator_I())

    if (eo is None):
        print "Object reference is not an Example::Echo"
        sys.exit(1)

    # logger.debug('ASAPIterator_I.next_n', exc_info=True, extra={'class': 'ASAPIterator_I',
    #                                                             'netxt_n': eo.next_n(10)})
    # logger.debug('ASAPIterator_I.getLength', exc_info=True, extra={'class': 'ASAPIterator_I',
    #                                                                'getLength': eo.getLength()})
    # logger.debug('ASAPIterator_I.destroy')


# class commonTestCase(TestCase):
#
#     # Resolve the name "test.my_context/ExampleEcho.Object"
#     name = [CosNaming.NameComponent("LocalNameContext", "my_context"),
#             CosNaming.NameComponent("common_Common_I", "Object")]
#     try:
#         obj = rootContext.resolve(name)
#         logger.debug('Object', exc_info=True, extra={'obj': obj})
#
#     except CosNaming.NamingContext.NotFound, ex:
#         logger.debug("Name not found")
#         sys.exit(1)
#
#     # Narrow the object to an Example::Echo
#     eo = obj#._narrow('Common_I')
#
#     if (eo is None):
#         print "Object reference is not an Common_I_i"
#         sys.exit(1)
#
#     lala = globaldefs.
#     # logger.debug('ASAPIterator_I.next_n', exc_info=True, extra={'class': 'ASAPIterator_I',
#     #                                                             'netxt_n': eo.next_n(10)})
#     # logger.debug('Common_I.setNativeEMSName', exc_info=True, extra={'class': 'Common_I',
#     #                                                                'setNativeEMSName':eo.setNativeEMSName(objectName='objectNmae', nativeEMSName=globaldefs_idl.NamingAttributes_T('NamingAttribute1','bcand',True))})
#     # logger.debug('Common_I.setUserLabel', exc_info=True, extra={'class': 'Common_I',
#     #                                                             'setNativeEMSName': eo.setNativeEMSName(globaldefs_idl.NamingAttributes_T('NamingAttribute1','bcand',True))})