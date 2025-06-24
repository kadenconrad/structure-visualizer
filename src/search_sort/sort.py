from . import *
TEST_CASES = [[32, 1, 20, 36, 72, 25, -3, 2, 4],[4, 1, 3, 9, 7], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [64, 34, 25, 5, 22, 11, 90, 12], [7, 12, 9, 11, 3], [38, 31, 20, 14, 30], [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0], ["hello", "a", "x", "b", "d", "c", "h", "k", "hi"]]

SORTED_CASES = [case.sorted() for case in TEST_CASES]

# Tests for insertion_sort
for i in range(len(TEST_CASES)):
    insertion_sort_passes = True
    ins_failed_cases = []
    ins_passed_cases = []
    result = insertion_sort(TEST_CASES[i])
    if result != SORTED_CASES[i]:
        insertion_sort_passes = False
        ins_failed_cases.append(TEST_CASES[i])
    else:
        ins_passed_cases.append(TEST_CASES[i])
if insertion_sort_passes == True:
    print(f"""Insertion Sort Grade: PASS ✅
        Passed cases: {ins_passed_cases}""")
else:
    print(f"""Insertion Sort Grade: FAIL ❌
        Passed case(s): {ins_passed_cases}
        Failed case(s): {ins_failed_cases}""")
    
# Tests for selection_sort
for i in range(len(TEST_CASES)):
    selection_sort_passes = True
    ss_failed_cases = []
    ss_passed_cases = []
    result = selection_sort(TEST_CASES[i])
    if result != SORTED_CASES[i]:
        selection_sort_passes = False
        ins_failed_cases.append(TEST_CASES[i])
    else:
        ins_passed_cases.append(TEST_CASES[i])
if selection_sort_passes == True:
    print(f"""Selection Sort Grade: PASS ✅
        Passed cases: {ss_passed_cases}""")
else:
    print(f"""Selection Sort Grade: FAIL ❌
        Passed case(s): {ss_passed_cases}
        Failed case(s): {ss_failed_cases}""")
    
# Tests for insertion_sort
for i in range(len(TEST_CASES)):
    quicksort_passes = True
    qs_failed_cases = []
    qs_passed_cases = []
    result = quicksort(TEST_CASES[i])
    if result != SORTED_CASES[i]:
        quicksort_passes = False
        qs_failed_cases.append(TEST_CASES[i])
    else:
        qs_passed_cases.append(TEST_CASES[i])
if quicksort_passes == True:
    print(f"""Quick Sort Grade: PASS ✅
        Passed cases: {qs_passed_cases}""")
else:
    print(f"""Quick Sort Grade: FAIL ❌
        Passed case(s): {qs_passed_cases}
        Failed case(s): {qs_failed_cases}""")
    
# Tests for merge_sort
for i in range(len(TEST_CASES)):
    merge_sort_passes = True
    ms_failed_cases = []
    ms_passed_cases = []
    result = merge_sort(TEST_CASES[i])
    if result != SORTED_CASES[i]:
        merge_sort_passes = False
        ms_failed_cases.append(TEST_CASES[i])
    else:
        ms_passed_cases.append(TEST_CASES[i])
if merge_sort_passes == True:
    print(f"""Merge Sort Grade: PASS ✅
        Passed cases: {ms_passed_cases}""")
else:
    print(f"""Merge Sort Grade: FAIL ❌
        Passed case(s): {ms_passed_cases}
        Failed case(s): {ms_failed_cases}""")

# Tests for shell_short
for i in range(len(TEST_CASES)):
    shell_sort_passes = True
    shs_failed_cases = []
    shs_passed_cases = []
    result = shell_sort(TEST_CASES[i])
    if result != SORTED_CASES[i]:
        shell_sort_passes = False
        shs_failed_cases.append(TEST_CASES[i])
    else:
        shs_passed_cases.append(TEST_CASES[i])
if shell_sort_passes == True:
    print(f"""Shell Sort Grade: PASS ✅
        Passed cases: {shs_passed_cases}""")
else:
    print(f"""Shell Sort Grade: FAIL ❌
        Passed case(s): {shs_passed_cases}
        Failed case(s): {shs_failed_cases}""")
    
