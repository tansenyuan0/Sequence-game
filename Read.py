##@file AALst.py
# @author Senyuan Tan
# @brief the stdntAllocTypes.py comes here
# @date  2019.02.09

from SALst import *
from DCapALst.py import *
from StdntAllocTypes.py import *

##brief  read the student information from the file
#param   source as the file name

def load_stdnt_data(source):
    SALst.init()
    file = open(source)
    std_info = file.readline()
    file.close()

    for info in std_info:
        Student_information = []
        temp_info = info.split(",")
        for element in temp_info:
            Student_information.append(element.strip())
        Student_information[5] = Student_information[5][1:]
        Student_information[-2] = Student_information[-2][:-1]
        student = SInfoT(
            Student_information[1],
            Student_information[2],
            Gent[Student_information[3]],
            float[Student_information[4]],
            SeqADT(Student_information[5:-2])
            (Student_information[-1] == "True")
        )
        SALst.add(Student_information[0], student)

##brief load dcap data is to load dcap from file
#param source as the filename

def load_dcap_data(source):
    DCapALst.init()
    file = open(source)
    dCap_info = file.readline()
    file.close()
    for info in dCap_info:
        information = []
        temp_info = info.split(",")
        for element in temp_info:
            information.append(element.strip())
        DCapALst.add(information[0],information[1])

