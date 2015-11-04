from TMF814_MTNM_IIS_R4_0_IDL.IDL import aSAP__POA
from TMF814_MTNM_IIS_R4_0_IDL.IDL.globaldefs_idl import ProcessingFailureException


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
