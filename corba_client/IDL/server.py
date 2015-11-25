# Initialise the ORB and find the root POA
import sys

import CosNaming
from omniORB import CORBA, PortableServer

import aSAP__POA
import callSNC__POA
import common__POA
import globaldefs_idl
from corba_client.IDL import common_idl

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

# Obtain a reference to the root naming context
obj = orb.resolve_initial_references("LightSoftNameService")
print orb.object_to_string(obj)

rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
    print "Failed to narrow the root naming context"
    sys.exit(1)

# name = [CosNaming.NameComponent("1LightSoftNameService", "ORG")]
# obj = rootContext.bind_new_context(name)
print orb.object_to_string(obj)

# Bind a context named "test.my_context" to the root context
name1 = [CosNaming.NameComponent("1stLocalNameContext", "1st_context")]
name2 = [CosNaming.NameComponent("2ndLocalNameContext", "2nd_context")]

try:
    testContext1 = rootContext.bind_new_context(name1)
    print "New test context bound: %s" %name1

except CosNaming.NamingContext.AlreadyBound, ex:
    print "Test context already exists: %s" %name1
    obj = rootContext.resolve(name1)
    testContext1 = obj._narrow(CosNaming.NamingContext)
    if testContext1 is None:
        print "test.mycontext exists but is not a NamingContext"
        sys.exit(1)

try:
    testContext2 = rootContext.bind_new_context(name2)
    print "New test context bound: %s" %name2

except CosNaming.NamingContext.AlreadyBound, ex:
    print "Test context already exists: %s" %name2
    obj = rootContext.resolve(name2)
    testContext2 = obj._narrow(CosNaming.NamingContext)
    if testContext2 is None:
        print "test.mycontext exists but is not a NamingContext"
        sys.exit(1)

# aSAP

class ASAPIterator_I_i(aSAP__POA.ASAPIterator_I):

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

# Create an instance of ASAPIterator_I_i and an Echo object reference
ob = ASAPIterator_I_i()
eo = ob._this()

# Bind the ASAPIterator_I_i object to the test context
name = [CosNaming.NameComponent("aSAP_ASAPIterator_I", "Object")]
try:
    testContext1.bind(name, eo)
    # testContext = rootContext.bind_new_context(name)
    print "New aSAP \nASAPIterator_I object bound %s" %name

except CosNaming.NamingContext.AlreadyBound:
    testContext1.rebind(name, eo)
    print "aSAP \nASAPIterator_I binding already existed -- rebound"


# callSNC

class CallAndTopLevelConnectionsIterator_I_i(callSNC__POA.CallAndTopLevelConnectionsIterator_I):

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

class CallAndTopLevelConnectionsAndSNCsIterator_I_i(callSNC__POA.CallAndTopLevelConnectionsAndSNCsIterator_I):

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

# Create an instance of CallAndTopLevelConnectionsIterator_I and an CallAndTopLevelConnectionsIterator_I object reference
ob = CallAndTopLevelConnectionsAndSNCsIterator_I_i()
eo = ob._this()

# Bind the ASAPIterator_I object to the test context
name = [CosNaming.NameComponent("callSNC_CallAndTopLevelConnectionsIterator_I", "Object")]
try:
    testContext1.bind(name, eo)
    # testContext = rootContext.bind_new_context(name)
    print "New callSNC \nCallAndTopLevelConnectionsIterator_I object bound %s" %name

except CosNaming.NamingContext.AlreadyBound:
    testContext1.rebind(name, eo)
    print "callSNC \nCallAndTopLevelConnectionsIterator_I binding already existed -- rebound"

# Create an instance of CallAndTopLevelConnectionsAndSNCsIterator_I and an CallAndTopLevelConnectionsAndSNCsIterator_I object reference
ob = CallAndTopLevelConnectionsAndSNCsIterator_I_i()
eo = ob._this()

# Bind the ASAPIterator_I_i object to the test context
name = [CosNaming.NameComponent("callSNC_CallAndTopLevelConnectionsAndSNCsIterator_I", "Object")]
try:
    testContext1.bind(name, eo)
    # testContext = rootContext.bind_new_context(name)
    print "New callSNC \nCallAndTopLevelConnectionsAndSNCsIterator_I object bound %s" %name

except CosNaming.NamingContext.AlreadyBound:
    testContext1.rebind(name, eo)
    print "callSNC \nCallAndTopLevelConnectionsAndSNCsIterator_I binding already existed -- rebound"


#common

class Common_I_i(common__POA.Common_I):

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
        print 'enforceUniqueness: ',enforceUniqueness

    # in globaldefs::NamingAttributes_T objectName,
    # in string owner)
    def setOwner(self, object_name, owner):
        print 'objectName: ',object_name
        print 'owner: ',owner

    # out CapabilityList_T capabilities)
    def getCapabilities(self):
        return common_idl.CapabilityList_T('capability1')

    # in globaldefs::NamingAttributes_T objectName,
    # inout globaldefs::NVSList_T additionalInfo)
    def setAdditionalInfo(self, objectName):
        print 'objectName: ',objectName
        return globaldefs_idl.NVSList_T('NVSList1')

# Create an instance of Common_I and an Common_I object reference
ob = Common_I_i()
eo = ob._this()

# Bind the Common_I object to the test context
name = [CosNaming.NameComponent("common_Common_I", "Object")]
try:
    testContext2.bind(name, eo)
    print "New common \nCommon_I object bound %s" %name

except CosNaming.NamingContext.AlreadyBound:
    testContext1.rebind(name, eo)
    print "common \nCommon_I binding already existed -- rebound"


# Activate the POA
poaManager = poa._get_the_POAManager()
poaManager.activate()

# Block for ever (or until the ORB is shut down)
orb.run()
