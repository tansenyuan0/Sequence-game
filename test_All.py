##@file test_All.py
# @author Senyuan Tan
# @brief the stdntAllocTypes.py comes here
# @date  2019.02.09

import pytest
from SALst import *
from DCapALst import *
from SeqADT import *
from StdntAllocTypes import *

## brief Runing test for SeqADT file and its function
class TestSeqADT:

    def setup_method(self, method):
        #setup the initial cases for every function
        self.sequence = SeqADT([DeptT.mechanical, DeptT.civil])
        self.empty = SeqADT([])

    def teardown_method(self, method):
        #teardown the initial cases
        self.sequence = None
        self.empty = None

    def test_init_method(self):
        #test for __init__ function
        assert self.sequence.seq == [DeptT.mechanical, DeptT.civil]
        assert self.sequence.count == 0

    def test_start_method(self):
        #test start function by testing count
        self.sequence.count = 4
        self.sequence.start()
        assert self.sequence.count == 0

    def test_next_method(self):
        # the first next
        assert self.sequence.next() == DeptT.mechanical
        assert self.sequence.count == 1

        # the second next
        self.sequence.next()
        assert self.sequence.next() == DeptT.civil
        assert self.sequence.count == 2

        # end with raise StopIteration
        with pytest.raises(StopIteration):
            self.sequence.next()

    def test_end_method(self):
        # test end function
        self.sequence.count = 2
        assert self.sequence.end()

    def test_init_empty(self):
        # test with empty list
        assert self.empty.seq == []
        assert self.empty.seq == 0

    def test_start_empty(self):
        # test start method with empty list
        self.empty.count = 2
        self.empty.start()
        assert self.empty.count == 0

    def test_next_empty(self):
        #test next method with empty list
        with pytest.raises(StopIteration):
            self.empty.next()

    def test_end_empty(self):
        #test end method with empty list
        assert self.empty.end()

## brief  test DCapALst file and its function
class TestDCapALst:

    def setup_method(self, method):
        # setup the initial case
        DCapALst.init()

    def test_init_method(self):
        # test init function
        DCapALst.init()
        assert DCapALst.seq == {}

    def test_add_method(self):
        # test add function
        DCapALst.add(DeptT.chemical, 4)
        assert DCapALst.seq == {DeptT.chemical: 4}
        with pytest.raises(KeyError):
            DCapALst.add(DeptT.chemical, 2)

    def test_remove_method(self):
        # test remove method
        DCapALst.seq = {DeptT.chemical : 5}
        assert DCapALst.remove(DeptT.chemical) == {}
        with pytest.raises(KeyError):
            DCapALst.remove(DeptT.civil)

    def test_elm_method(self):
        # test elm method
        DCapALst.seq = {DeptT.chemical: 2}
        assert DCapALst.elm(DeptT.chemical)

    def test_capacity_method(self):
        #test capacity method
        DCapALst.seq = {DeptT.chemical: 3}
        assert DCapALst.capacity(DeptT.chemical) == 3

## brief test SALst file and its fucntion
class TestSALst:

    def setup_method(self, method):
        # set up the initial case
        SALst.init()


    def test_init_method(self):
        # test the init function
        SALst.init()
        assert SALst.seq == {}

    def test_add_method(self):
        # test the add function
        SALst.add("Alex12", ("Alex", "Tan", GenT.male, 1.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), True))
        assert SALst.seq == {"Alex12": ("Alex", "Tan", GenT.male, 1.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), True)}
        with pytest.raises(KeyError):
            SALst.add("Alex12", ("Alex", "Tan", GenT.male, 1.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), True))

    def test_remove_method(self):
        #  test remove function
        SALst.seq = {"Alex12": ("Alex", "Tan", GenT.male, 1.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), True)}
        SALst.romove("Alex12")
        assert SALst.seq == {}
        with pytest.raises(KeyError):
            SALst.romove("Alice12")

    def test_elm_method(self):
        # test elm function
        SALst.seq = {"Alex12": ("Alex", "Tan", GenT.male, 1.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), True)}
        assert SALst.elm("Alex12")

    def test_info_method(self):
        # test info function
        SALst.seq = {"Alex12": ("Alex", "Tan", GenT.male, 1.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), True)}
        assert SALst.info("Alex12") == ("Alex", "Tan", GenT.male, 1.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), True)
        with pytest.raises(KeyError):
            SALst.info("Alice12")

    def test_sort_method(self):
        # test sort function
        seq1 = SInfoT("Alex", "Tan", GenT.male, 1.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), True)
        seq2 = SInfoT("Alice", "Tan", GenT.female, 12.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), false)
        seq3 = SInfoT("Trace", "Tan", GenT.female, 7.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), false)
        SALst.seq = {"Alex12": seq1, "Alice12": seq2, "Trace12": seq3}
        result = SALst.sort(lambda t:(t.freechoice) and (t.gpa > 4.0))
        assert result == {}

    def test_sort_boundary(self):
        # test sort boundary
        seq1 = SInfoT("Alex", "Tan", GenT.male, 1.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), True)
        seq2 = SInfoT("Alice", "Tan", GenT.female, 12.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), false)
        seq3 = SInfoT("Trace", "Tan", GenT.female, 7.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), false)
        SALst.seq = {"Alex12": seq1, "Alice12": seq2, "Trace12": seq3}
        result = SALst.sort(lambda t:(not t.freechoice) and (t.gpa > 4.0))
        assert result == ["Alice12", "Trace12"]

    def test_average_method(self):
        # test aveerage function
        seq1 = SInfoT("Alex", "Tan", GenT.male, 1.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), True)
        seq2 = SInfoT("Alice", "Tan", GenT.female, 12.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), false)
        seq3 = SInfoT("Trace", "Tan", GenT.female, 7.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), false)
        SALst.seq = {"Alex12": seq1, "Alice12": seq2, "Trace12": seq3}
        result = SALst.average(lambda t:(t.freechoice) and (t.gpa > 4.0))
        assert result == 0

    def test_average_boundary(self):
        # test average boundary
        seq1 = SInfoT("Alex", "Tan", GenT.male, 1.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), True)
        seq2 = SInfoT("Alice", "Tan", GenT.female, 12.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), false)
        seq3 = SInfoT("Trace", "Tan", GenT.female, 7.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), false)
        SALst.seq = {"Alex12": seq1, "Alice12": seq2, "Trace12": seq3}
        result = SALst.average(lambda t:(not t.freechoice) and (t.gpa > 4.0))
        assert result == 9.5

    def test_allocate_method(self):
        #test allocate funcction
        DCapALst.seq = {
            DeptT.civil: 1, DeptT.chemical: 1, DeptT.mechanical: 1
        }
        seq1 = SInfoT("Alex", "Tan", GenT.male, 6.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), True)
        seq2 = SInfoT("Alice", "Tan", GenT.female, 12.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), false)
        seq3 = SInfoT("Trace", "Tan", GenT.female, 7.0, (DeptT.chemical, DeptT.civil, DeptT.mechanical), false)
        SALst.seq = {"Alex12": seq1, "Alice12": seq2, "Trace12": seq3}
        result = {DeptT.civil: ["Alice12"], DeptT.chemical: ["Alex12"],
                  DeptT.electrical: [], DeptT.mechanical: [],
                  DeptT.software: [], DeptT.materials: ["Trace12"],
                  DeptT.engphys: []}
        SALst.allocate()
        assert AALst == result