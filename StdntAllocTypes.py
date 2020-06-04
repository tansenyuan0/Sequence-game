##@file stdntAllocTypes.py
# @author Senyuan Tan
# @brief the stdntAllocTypes.py comes here
# @date  2019.02.09

#import the function we need to use from the library
from SeqADT import *
from enum import Enum
from typing import NamedTuple

##brief stdntAllocTypes define three more class that helps input gender, departure and student information
#param  GenT, DeptT, SInfoT are three param that can use as function that define the gender, department and student information
#return  No return
class StdntAllocTypes:

##brief  GenT define the gender of student
#param Enum used to use enumeration to create enumerated constants
#return  No return
    class GenT(Enum):
        male = "male"
        female = "female"

##brief  DeptT define the departure that student's choice
#param Enum used to use enumeration to create enumerated constants
#return  No return

    class DeptT(Enum):
        civil = "civil"
        chemical = "chemical"
        electrical = "electrical"
        mechanical = "mechanical"
        software = "software"
        material = "material"
        engphys = "engphys"

##brief SInfoT define the student information
#param Enum used to use enumeration to create enumerated constants
#return No return

    class SInfoT(NamedTuple):
        fname: str
        lname: str
        gender: GenT
        gpa: float
        choice: type(SeqADT(DeptT))
        freechoice: bool




    