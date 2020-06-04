##@file DCapALst.py
# @author Senyuan Tan
# @brief the stdntAllocTypes.py comes here
# @date  2019.02.09

##brief define the class DcapALst to get access to the departure capacity
#param  function that can get access to the list, such as, add, remove.
#return   Return the Departure capacity list after get in the information
class DCapALst:

##brief init fucntion to define the sequence as a dictionary
#param no parameter
#return with no return
    @staticmethod
    def init():
        DCapALst.seq = {}

##brief add function to add dept name and capacity inside of the dictionary
#param dept as the departure name, cap as integer with the capacity of the departure
#return return KeyError if the dept is already in the dictionary
    @staticmethod
    def add(dept, cap):
        if dept in DCapALst.seq:
            raise KeyError
        else:
            DCapALst.seq[dept] = cap

##brief remove function to remove the dept and capacity from the dictionary
#param dept as the departure name, also as the key
#return KeyError if the departure is not inside of the dictionary
    @staticmethod
    def remove(dept):
        if dept in DCapALst.seq:
            del DCapALst.seq[dept]
        else:
            raise KeyError

##brief elm function to find if dept is in the dictionary
#param dept as the departure name, also as the key
#return  return True if dept in the dictionary, otherwise return False
    @staticmethod
    def elm(dept):
        if dept in DCapALst.seq:
            return True
        else:
            return False

##brief capcaity function to return the departure capacity
#param dept as the departure name, also as the key
#return return the departure capacity if dept inside of the dictionary,else return Key Error
    @staticmethod
    def capacity(dept):
        if dept in DCapALst.seq:
            return DCapALst.seq[dept]
        else:
            raise KeyError