"""Test my zip function! """

from lessons.zip import zip

"""Edge Case: Testing if zip is given an empty list, does it returns an empty dictionary?"""
def test1_empty_list():
    list_a = []
    list_b = []
    assert zip(list_a, list_b) == {}


"""Use Case: Testing if zip is given lists of different lengths, does it return an empty dictionary?"""
def test2_different_length_lists():
    list_a = ["hi", "bye"]
    list_b = [1, 2, 3]
    assert zip(list_a, list_b) == {}


"""Use Case: Testing if zip is given lists of the same lengths, does it return a dictionary that corresponds by index?"""
def test3_two_lists():
    list_a = ["hi", "bye", "hello" ]
    list_b = [1, 2, 3]
    assert zip(list_a, list_b) == {"hi": 1, "bye": 2, "hello": 3}