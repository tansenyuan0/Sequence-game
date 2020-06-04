##@file AALst.py
# @author Senyuan Tan
# @brief the stdntAllocTypes.py comes here
# @date  2019.02.09

from StdntAllocTypes import *

##brief AALst is used as the class and it is used to as the list that contain the student's choice of departure
#param  with no param
#return  with no return
class AALst:

##brief init function used to initial the set up of the departure.
#param  with no parameter
#return  with no return
    @staticmethod
    def init():
        AALst.seq = {
            DeptT.civil: [], DeptT.chemical: [], DeptT.electrical: [], DeptT.mechanical: [], DeptT.software:[], DeptT.material:[],DeptT.engphys:[]
        }

##brief add_stdnt() to add student's info inside of the departure
#param  dept and string that dept as the departure name and string as the student's name
# return  no return
    @staticmethod
    def add_stdnt(dept,string):
        AALst.seq[dept].append(string)

##brief lst_alloc function is to alloc the dept that print out the name of student inside of the dept
#param dept is the name of the departure
#return  the value of dept which is the name of student.
    @staticmethod
    def lst_alloc(dept):
        if dept in AALst.seq:
            return AALst.seq[dept]

##brief num_alloc function is to use to count the number of student inside of the departure
#param dept is the name of the departure
#return the number of student inside of the departure
    @staticmethod
    def num_alloc(dept):
        if dept in AALst.seq:
            return len(AALst.seq[dept])

