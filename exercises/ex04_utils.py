"""Exercise 4: List Utility Functions Practice"""
__author__ = "730324119"

test_int: int = 2
test_list_of_ints: int = [2,2,2]
test2_list_of_ints: int = [1,2,2]

def all(list_ints, single_int) -> bool:
    if(len(list_ints)==0):
        return False
    index: int = 0
    while index < len(list_ints):
        if list_ints[index] != single_int:
            return False
        index += 1
    return True

def max(list_ints) -> int:
    if len(list_ints) == 0:
        raise ValueError('max() arg is an empty List')
    max_value: int = 0
    index: int = 0
    while index < len(list_ints):
        if list_ints[index] > max_value:
            max_value = list_ints[index]
        index += 1
    return max_value

def is_equal(list1, list2) -> bool:
    if len(list1) != len(list2):
        return False
    index = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1
    return True

def main():
    print(all(test_list_of_ints, test_int))
    print(max(test_list_of_ints))
    print(is_equal(test_list_of_ints, test2_list_of_ints))

main()