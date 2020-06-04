## @file sSeqADT.py
# @author Senyuan Tan
# @brief the stdntAllocTypes.py comes here
# @date  2019.02.09

## @brief SeqADT is used to define it self and the counter
# @param set up function with start and next function
# @return no return
class SeqADT:

## @brief __init__ define itself
# @param x is used to define count and sequence of x
# @return no return
    def __init__(self, x):
        self.seq = x
        self.count = 0

## @brief start function was used to start the count
# @param no parameter
# @return no return
    def start(self):
        self.count = 0

## @brief next function was used to add one more count if the self is not end
# @param no parameter
# @return the last element in the sequence
    def next(self):
        if(self.end()):
            raise StopIteration
        else:
            self.count += 1
            return self.seq(self.count - 1)
## @brief end the function while count is larger than the sequence itself
# @param  no parameter
# @return no return
    def end(self):
        return self.count >= len(self.seq)