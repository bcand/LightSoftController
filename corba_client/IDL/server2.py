# Initialise the ORB and find the root POA
import sys

import CosNaming
from omniORB import CORBA, PortableServer

import aSAP__POA
import callSNC__POA
import common__POA
import globaldefs
import common_idl

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

# Activate the POA
poaManager = poa._get_the_POAManager()

# Obtain a reference to the root naming context
obj = orb.resolve_initial_references("NameService")
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
    eo = object#ob._this()
    print 'Object', obj

    # Bind the object to the test context
    name = [CosNaming.NameComponent(object_name, object_type)]
    try:
        context.bind(name, eo)
        print "New ", name, "object bound "

    except CosNaming.NamingContext.AlreadyBound:
        context.rebind(name, eo)
        print name, " binding already existed -- rebound"

def add_new_POA(servant, object_name, poa):
    # Create a POA for the game and its associated objects.
    # Default policies are suitable. Having one POA per game makes
       # it easy to deactivate all objects associated with a game.
    try:
        local_poa = poa.create_POA(object_name, None, [])

        # # Create servant object
        # servant = object_name, '_impl'()

        # Activate it
        id = local_poa.activate_object(servant)

        # Get the object reference
        obj = local_poa.id_to_reference(id)

        # Activate the POA
        local_poa._get_the_POAManager().activate()
    except globaldefs.ProcessingFailureException, ex:
            print ex

    return obj

# aSAP


class ASAPIterator_I_impl(aSAP__POA.ASAPIterator_I):

    def next_n(self, how_many, aSAPList):
        try:
            print 'next_n called with :', how_many ,aSAPList
            flag = True
        except globaldefs.ProcessingFailureException, ex:
            print ex
            flag = False
        return flag

    def getLength(self):
        try:
            print 'getLength called'
            length = 10
        except globaldefs.ProcessingFailureException, ex:
            print ex
        return length

    def destroy(self):
        try:
            print 'destroy called'
        except Exception, ex:
            print ex
servant = ASAPIterator_I_impl()
obj = add_new_POA(servant, 'ASAPIterator_I', poa)
bind_in_context(obj, "ASAPIterator_I",
                 "Object", testContext)

# callSNC

class CallAndTopLevelConnectionsIterator_I_impl(callSNC__POA.CallAndTopLevelConnectionsIterator_I):

    def next_n(self, how_many, aSAPList):
        try:
            print 'next_n called with :', how_many, aSAPList
            flag = True
        except globaldefs.ProcessingFailureException, ex:
            print ex
            flag = False
        return flag

    def getLength(self):
        try:
            print 'getLength called'
            length = 10
        except globaldefs.ProcessingFailureException, ex:
            print ex
        return length

    def destroy(self):
        try:
            print 'destroy called'
        except globaldefs.ProcessingFailureException, ex:
            print ex

class CallAndTopLevelConnectionsAndSNCsIterator_I_impl(callSNC__POA.CallAndTopLevelConnectionsAndSNCsIterator_I):

    def next_n(self, how_many, aSAPList):
        try:
            print 'next_n called with :', how_many ,aSAPList
            flag = True
        except globaldefs.ProcessingFailureException, ex:
            print ex
            flag = False
        return flag

    def getLength(self):
        try:
            print 'getLength called'
            length = 10
        except globaldefs.ProcessingFailureException, ex:
            print ex
        return length

    def destroy(self):
        try:
            print 'destroy called'
        except globaldefs.ProcessingFailureException, ex:
            print ex
servant = CallAndTopLevelConnectionsIterator_I_impl()
obj = add_new_POA(servant, 'CallAndTopLevelConnectionsIterator_I', poa)
bind_in_context(obj,
                 "CallAndTopLevelConnectionsIterator_I", "Object", testContext)
servant = CallAndTopLevelConnectionsIterator_I_impl()
obj = add_new_POA(servant, 'CallAndTopLevelConnectionsAndSNCsIterator_I', poa)
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
        except globaldefs.ProcessingFailureException, ex:
            print ex

    # out CapabilityList_T capabilities)
    def getCapabilities(self):
        return common_idl.CapabilityList_T('capability1')

    # in globaldefs::NamingAttributes_T objectName,
    # inout globaldefs::NVSList_T additionalInfo)
    def setAdditionalInfo(self, objectName):
        print 'objectName: ', objectName
        return globaldefs.NVSList_T('NVSList1')
servant = Common_I_impl()
obj = add_new_POA(servant, 'Common_I', poa)
bind_in_context(obj, "Common_I",
                 "Object", testContext)
# poa.activate_object(obj)




poaManager.activate()

# Block for ever (or until the ORB is shut down)
orb.run()
print 'Server is up'