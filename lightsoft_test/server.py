# Initialise the ORB and find the root POA
import sys

import CosNaming
from IDL.globaldefs_idl import ProcessingFailureException
from omniORB import CORBA

from corba_client.IDL import aSAP__POA


class ASAPIterator_I_i(aSAP__POA.ASAPIterator_I):

    def next_n( how_many, aSAPList):
        try:
            print 'next_n called with :', how_many ,aSAPList
            flag = True
        except ProcessingFailureException, ex:
            print ex
            flag = False
        return flag

    def getLength(self):
        try:
            print 'getLength called'
            length = 10
        except ProcessingFailureException, ex:
            print ex
        return length

    def destroy(self):
        try:
            print 'destroy called'
        except ProcessingFailureException, ex:
            print ex

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")


# Create an instance of Echo_i and an Echo object reference
aSAPi = ASAPIterator_I_i()
eo = aSAPi._this()

# Obtain a reference to the root naming context
obj = orb.resolve_initial_references("NameService")
print orb.object_to_string(obj)
rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
    print "Failed to narrow the root naming context"
    sys.exit(1)

# Bind a context named "test.my_context" to the root context
name = [CosNaming.NameComponent("LocalNameContext", "my_context")]
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
name = [CosNaming.NameComponent("aSAR_stabASAPIterator_I_i", "Object")]
try:
    testContext.bind(name, eo)
    # testContext = rootContext.bind_new_context(name)
    print "New ExampleEcho object bound %s" %name

except CosNaming.NamingContext.AlreadyBound:
    testContext.rebind(name, eo)
    print "ExampleEcho binding already existed -- rebound"

# Activate the POA
poaManager = poa._get_the_POAManager()
poaManager.activate()

# Block for ever (or until the ORB is shut down)
orb.run()
