"""Combining two lists into a dictionary!"""
__author__ = 730324119

dictionary: dict[str, int] = {}


def zip(list_a: list[str], list_b: list[int]) -> dict[str, int]:
    """Produce a dictionary where the keys are the items of the first list and the values are the corresponding items at the same index of the second list!"""
    if len(list_a) != len(list_b):
        return {}
    if len(list_a or list_b) < 1:
        return {}
    else: 
        index = 0
        while index < len(list_a):
            newKey = list_a[index]
            newValue = list_b[index]
            dictionary[newKey] = (newValue)
            index += 1
        return dictionary
    

print(zip(["Tuesday", "Happy"], [1, 2]))