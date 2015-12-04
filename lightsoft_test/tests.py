import CosNaming
import sys

from django.test import TestCase
from raven.contrib.django.raven_compat.models import logging

from corba_client.globaldefs_impl import NameAndStringValue_T, NVSList_T, NamingAttributes_T
# from corba_client.globaldefs_impl import  NameAndStringValue_T
from corba_client.client import Client
# from corba_client.IDL import globaldefs
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

# class all_togetherTestcase(TestCase):
#     client = Client(None, "NameService")
#     obj = client.get_resolved_object("Local_Context", "my_context", "ASAPIterator_I", "Object")
#     print 'getLength: ', obj.getLength()
#
#     client = Client(None, "NameService")
#     obj = client.get_resolved_object("Local_Context", "my_context", "Common_I", "Object")
#     print 'setOwner: ', obj.setOwner()

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
    client = Client(None, "NameService")
    obj = client.get_resolved_object("Local_Context", "my_context", "CallAndTopLevelConnectionsAndSNCsIterator_I", "Object")
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
    nsv1 = NameAndStringValue_T('lala', 'kaka')
    nsv2 = NameAndStringValue_T('pop', 'lock')
    # nsv = globaldefs.NameAndStringValue_T('lala', 'kaka')
    # print nsv

    # nsvl = [[ ('lala', 'kaka']]
    nsvl = NVSList_T(nsv1, nsv2)
    na = NamingAttributes_T()
    na = nsvl
    print 'setOwner: ', obj.setOwner(na, 'bcand')
    print 'lala: ',obj
    # eo.setOwner("lala", "bcand")

    # logger.debug('ASAPIterator_I.next_n', exc_info=True, extra={'class': 'ASAPIterator_I',
    #                                                             'netxt_n': eo.next_n(10)})
    # logger.debug('Common_I.setNativeEMSName', exc_info=True, extra={'class': 'Common_I',
    #                                                                'setNativeEMSName':eo.setNativeEMSName(objectName='objectNmae', nativeEMSName=globaldefs_idl.NamingAttributes_T('NamingAttribute1','bcand',True))})
    # logger.debug('Common_I.setUserLabel', exc_info=True, extra={'class': 'Common_I',
    #                                                             'setNativeEMSName': eo.setNativeEMSName(globaldefs_idl.NamingAttributes_T('NamingAttribute1','bcand',True))})



# class callSNCTestCaseWithStringified(TestCase):
#     client = Client(None, "NameService")
#     ior = "IOR:010000004d00000049444c3a6d746e6d2e746d666f72756d2e6f72672f63616c6c534e432f43616c6c416e64546f704c6576656c436f6e6e656374696f6e73416e64534e43734974657261746f725f493a312e3000000000010000000000000068000000010102000f0000003139352e3133342e36372e3136390000f69b00000e000000feaa3e585600003ddf000000000100000200000000000000080000000100000000545441010000001c00000001000000010001000100000001000105090101000100000009010100"
#
#     obj = client.get_resolved_object_by_Stringified(ior)
#     print 'getLength: ', obj.getLength()
#     client = None
#     # logger.debug('ASAPIterator_I.next_n', exc_info=True, extra={'class': 'ASAPIterator_I',
#     #                                                             'netxt_n': eo.next_n(10)})
#     # logger.debug('ASAPIterator_I.getLength', exc_info=True, extra={'class': 'ASAPIterator_I',
#     #                                                                'getLength': eo.getLength()})
#     # logger.debug('ASAPIterator_I.destroy')
