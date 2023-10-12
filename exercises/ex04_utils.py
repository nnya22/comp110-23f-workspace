"""Exercise 4: List Utility Functions Practice!"""
__author__ = "730324119"


def all(list_ints: list[int], single_int: int) -> bool:
    """Checks the list of integers to ensure every integer matches the single integer."""
    if (len(list_ints) == 0):
        return False
    index: int = 0
    while index < len(list_ints):
        if list_ints[index] != single_int:
            return False
        index += 1
    return True


def max(list_ints: list[int]) -> int:
    """Determines the integer within the list that has the maximum value."""
    if len(list_ints) == 0:
        raise ValueError("max() arg is an empty List")
    max_value: int = list_ints[0]
    index: int = 0
    while index < len(list_ints):
        if list_ints[index] > max_value:
            max_value = list_ints[index]
        index += 1
    return max_value


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Ensures that each each element at every index is equal in both lists."""
    if len(list1) != len(list2):
        return False
    index = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1
    return True