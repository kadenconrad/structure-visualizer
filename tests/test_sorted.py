from src.search_sort import *
import pytest
from random import randint
from src.models._array import Array

case1 = Array("uint", 9)
case1.populate()
case2 = Array("int", 5)
case2.populate()
case3 = Array("int", 10)
case3.populate()
case4 = Array("int", 8)
case4.populate()
case5 = Array("int", 5)
case5.populate()
case6 = Array("int", 12) # zeros
for i in range(case6.size):
    case6.set_index(i, 0)
case7 = Array("str", 9, max_str_length=7)
case7.populate()
case8 = Array("double", 6)
case8.populate()

TEST_CASES = [case1, case2, case3, case4, case5, case6, case7, case8]


SORTED_CASES = []
for i in range(len(TEST_CASES)):
    case = TEST_CASES[i]
    if case.array_type != "str":
        SORTED_CASES.append(list(sorted(case.memory)))
    else:
        str_arr = [case.get_index_data(i) for i in range(case.size)]
        SORTED_CASES.append(list(sorted(str_arr)))


def test_insertion_sort():
    for i in range(len(TEST_CASES)):
        result = insertion_sort.insertion_sort(TEST_CASES[i])
        result_list = [result.get_index_data(j) for j in range(result.size)]
        assert result_list == SORTED_CASES[i], f"{TEST_CASES[i]} failed ❌ Expected result: {SORTED_CASES[i]}"
    

def test_selection_sort():
    for i in range(len(TEST_CASES)):
        result = selection_sort.selection_sort(TEST_CASES[i])
        result_list = [result.get_index_data(j) for j in range(result.size)]
        assert result_list == SORTED_CASES[i], f"{TEST_CASES[i]} failed ❌ Expected result: {SORTED_CASES[i]}"
    

def test_quicksort():
    for i in range(len(TEST_CASES)):
        result = quicksort.quicksort(TEST_CASES[i])
        result_list = [result.get_index_data(j) for j in range(result.size)]
        assert result_list == SORTED_CASES[i], f"{TEST_CASES[i]} failed ❌ Expected result: {SORTED_CASES[i]}"
    

def test_merge_sort():
    for i in range(len(TEST_CASES)):
        result = merge_sort.merge_sort(TEST_CASES[i])
        result_list = [result.get_index_data(j) for j in range(result.size)]
        assert result_list == SORTED_CASES[i], f"{TEST_CASES[i]} failed ❌ Expected result: {SORTED_CASES[i]}"


def test_shell_sort():
    for i in range(len(TEST_CASES)):
        result = shell_sort.shell_sort(TEST_CASES[i])
        result_list = [result.get_index_data(j) for j in range(result.size)]
        assert result_list == SORTED_CASES[i], f"{TEST_CASES[i]} failed ❌ Expected result: {SORTED_CASES[i]}"

def test_binary_search():
    for i in range(len(TEST_CASES)):
        idx = randint(0, TEST_CASES[i].size - 1)
        target = TEST_CASES[i].get_index_data(idx)
        result = binary_search.binary_search(TEST_CASES[i], target)
        assert result == idx or -1, f"Expected result: {idx if idx < TEST_CASES[i].size else -1}; returned result: {result}."
