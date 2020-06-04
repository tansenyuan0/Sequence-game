##@file SALst.py
# @author Senyuan Tan
# @brief the stdntAllocTypes.py comes here
# @date  2019.02.09

from StdntAllocTypes import *
from AALst import *
from DCapALst import *
from operator import itemgetter

##brief SALst is the class that cantain the function that it will access the student allocation into the departure
#param  with no parameter
#return with no return

class SALst():

##brief init is the function that set up the sequence as the dictionary for SALst
#param   with no parameter
#return  with no return
    @staticmethod
    def init():
        SALst.seq = {}

##brief add is the function that add student information into the dictionary
#param  string as the student name, inf is the information that we define in StdntAllocTypes
#return KeyError if the student is already inside the dictionary
    @staticmethod
    def add(string, inf):
        if SALst.elm(string):
            raise KeyError
        else:
            SALst.seq[string] = inf

##brief remove function is used to remove student's information from the dictionary
#param   string as the student's name
#return  KeyError if the student is not in the dictionary
    @staticmethod
    def remove(string):
        if SALst.elm(string):
            del SALst.seq[string]
        else:
            raise KeyError

##breif  elm function is used to determine if the student whether he is inside of the dictionary or not
#param string as the student's name
#return True if student insode of dictionary, false otherwise.
    @staticmethod
    def elm(string):
        if string in SALst.seq:
            return True
        else:
            return False

##brief  info function is used to return the information of the student
#param   string as the student's name
#return  return the student's information if it is inside of dictionary, else return KeyError
    @staticmethod
    def info(string):
        if SALst.elm(string):
            return SALst.seq[string]
        else:
            raise KeyError

##brief  sort function is used to sort student in decending order according to his gpa
#param  info is the student that which will be used to be sorted
#return  return the list that is sorted
    @staticmethod
    def sort(condition):
        std_list = []
        id = SALst.seq.keys()
        list = []
        for i in id:
            if condition(SALst.seq[i]):
                std_list.append({"id":i, "grade":SALst.seq[i].gpa})
        std_list.sort(key = itemgetter("grade"), reverse = True)
        for x in std_list:
            list.append(item["id"])
        return list


##brief average function is used to calculate the average gpa of the class
#param  info as the student info that which student are being used to calculation
#return  return the average gpa and if there is no student raise ValueError
    @staticmethod
    def average(condition):
        sum = 0
        id_list = SALst.seq.keys()
        count = 0
        for m in id_list:
            if condition(SALst.seq[m]):
                sum += SALst.seq[m].gpa
            count += 1
        avg = float(sum/count)
        if avg > 0:
            return avg
        else:
            raise ValueError

##brief  allocate function is used to allocate student's choice of the departure
#param  no parameter
#return RuntimeError if the student cannot be allocate if the capacity of the departure are full for all three
    @staticmethod
    def allocate():
        AALst.init()
        f = SALst.sort(lambda t: (t.freechoice) and t.gpa >= 4.0)
        for m in f:
            ch = SALst.info(m).choices
            AALst.add_stdnt(ch.next(), m)

        s = SALst.sort(lambda t: (not t.freechoice) and t.gpa >= 4.0)
        for m in S_list:
            ch = SALst.info(m).choices
            alloc = False
            while (not alloc) and  (not ch.end()):
                d = ch.next()
                if AALst.num_alloc(d) < DCapALst.capacity(d):
                    AALst.add_stdnt(d,m)
                    alloc = True
                else:
                    raise RuntimeError