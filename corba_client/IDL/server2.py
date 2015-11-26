# Initialise the ORB and find the root POA
import sys

import CosNaming
from omniORB import CORBA, PortableServer

import aSAP__POA
import callSNC__POA
import common__POA
import globaldefs_idl
import common_idl

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

# Obtain a reference to the root naming context
obj = orb.resolve_initial_references("LightSoftNameService")
print orb.object_to_string(obj)

rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
    print "Failed to narrow the root naming context"
    sys.exit(1)

# Bind a context named "test.my_context" to the root context
name = [CosNaming.NameComponent("Local_Context", "my_context")]
try:
    testContext = rootContext.bind_new_context(name)
    print "New test context bound: %s" %name

except CosNaming.NamingContext.AlreadyBound, ex:
    print "Test context already exists: %s" %name
    obj = rootContext.resolve(name)
    testContext = obj._narrow(CosNaming.NamingContext)

if testContext is None:
        print "test.mycontext exists but is not a NamingContext"
        sys.exit(1)


def bind_in_context(object, object_name, object_type, context):
    # Create an instance of the object and an object reference
    ob = object
    eo = ob._this()
    print 'Object', obj

    # Bind the object to the test context
    name = [CosNaming.NameComponent(object_name, object_type)]
    try:
        context.bind(name, eo)
        print "New ", name, "object bound "

    except CosNaming.NamingContext.AlreadyBound:
        context.rebind(name, eo)
        print name, " binding already existed -- rebound"


# aSAP


class ASAPIterator_I_impl(aSAP__POA.ASAPIterator_I):

    def next_n(self, how_many, aSAPList):
        try:
            print 'next_n called with :', how_many ,aSAPList
            flag = True
        except globaldefs_idl.ProcessingFailureException, ex:
            print ex
            flag = False
        return flag

    def getLength(self):
        try:
            print 'getLength called'
            length = 10
        except globaldefs_idl.ProcessingFailureException, ex:
            print ex
        return length

    def destroy(self):
        try:
            print 'destroy called'
        except globaldefs_idl.ProcessingFailureException, ex:
            print ex
obj = ASAPIterator_I_impl()
bind_in_context(obj, "ASAPIterator_I",
                 "Object", testContext)

# callSNC

class CallAndTopLevelConnectionsIterator_I_impl(callSNC__POA.CallAndTopLevelConnectionsIterator_I):

    def next_n(self, how_many, aSAPList):
        try:
            print 'next_n called with :', how_many, aSAPList
            flag = True
        except globaldefs_idl.ProcessingFailureException, ex:
            print ex
            flag = False
        return flag

    def getLength(self):
        try:
            print 'getLength called'
            length = 10
        except globaldefs_idl.ProcessingFailureException, ex:
            print ex
        return length

    def destroy(self):
        try:
            print 'destroy called'
        except globaldefs_idl.ProcessingFailureException, ex:
            print ex

class CallAndTopLevelConnectionsAndSNCsIterator_I_impl(callSNC__POA.CallAndTopLevelConnectionsAndSNCsIterator_I):

    def next_n(self, how_many, aSAPList):
        try:
            print 'next_n called with :', how_many ,aSAPList
            flag = True
        except globaldefs_idl.ProcessingFailureException, ex:
            print ex
            flag = False
        return flag

    def getLength(self):
        try:
            print 'getLength called'
            length = 10
        except globaldefs_idl.ProcessingFailureException, ex:
            print ex
        return length

    def destroy(self):
        try:
            print 'destroy called'
        except globaldefs_idl.ProcessingFailureException, ex:
            print ex
obj = CallAndTopLevelConnectionsAndSNCsIterator_I_impl()
bind_in_context(obj,
                 "CallAndTopLevelConnectionsIterator_I", "Object", testContext)
obj = CallAndTopLevelConnectionsAndSNCsIterator_I_impl()
bind_in_context(obj,
                 "CallAndTopLevelConnectionsAndSNCsIterator_I", "Object", testContext)


# common


class Common_I_impl(common__POA.Common_I):

    # in globaldefs::NamingAttributes_T objectName,
    # in string nativeEMSName)
    def setNativeEMSName(self, objectName, nativeEMSName):
        print 'objectName: ',objectName
        print 'nativeEMSName :',nativeEMSName

    # in globaldefs::NamingAttributes_T objectName,
    # in string userLabel,
    # in boolean enforceUniqueness)
    def setUserLabel (self, objectName, userLabel, enforceUniqueness):
        print 'objectName: ', objectName
        print 'userLabel: ', userLabel
        print 'enforceUniqueness: ', enforceUniqueness

    # in globaldefs::NamingAttributes_T objectName,
    # in string owner)
    def setOwner(self, object_name, owner):
        try:
            print 'objectName: ', object_name
            print 'owner: ', owner
        except globaldefs_idl.ProcessingFailureException, ex:
            print ex

    # out CapabilityList_T capabilities)
    def getCapabilities(self):
        return common_idl.CapabilityList_T('capability1')

    # in globaldefs::NamingAttributes_T objectName,
    # inout globaldefs::NVSList_T additionalInfo)
    def setAdditionalInfo(self, objectName):
        print 'objectName: ', objectName
        return globaldefs_idl.NVSList_T('NVSList1')

obj = Common_I_impl()
bind_in_context(obj, "Common_I",
                 "Object", testContext)




# Activate the POA
poaManager = poa._get_the_POAManager()
poaManager.activate()

# Block for ever (or until the ORB is shut down)
orb.run()
