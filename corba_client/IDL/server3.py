import sys
from omniORB import CORBA, PortableServer, orb
import CosNaming
#
# # Define an implementation of the Echo interface
# from corba_api import Example__POA
#
#
import aSAP__POA
import globaldefs_idl


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

# Initialise the ORB and find the root POA
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")


# Create an instance of ASAPIterator_I_i and an Echo object reference
ob = ASAPIterator_I_i()
eo = ob._this()

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

# Bind the Echo object to the test context
name = [CosNaming.NameComponent("aSAP_ASAPIterator_I", "Object")]
try:
    testContext.bind(name, eo)
    # testContext = rootContext.bind_new_context(name)
    print "New aSAP_ASAPIterator_I object bound %s" %name

except CosNaming.NamingContext.AlreadyBound:
    testContext.rebind(name, eo)
    print "aSAP_ASAPIterator_I binding already existed -- rebound"

# Activate the POA
poaManager = poa._get_the_POAManager()
poaManager.activate()

# Block for ever (or until the ORB is shut down)
orb.run()
