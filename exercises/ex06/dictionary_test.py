"""Testing edge and use cases for my dictionary functions!"""

__author__ = "730324119"

from exercises.ex06.dictionary import invert

"""Invert Edge Case: Test if the function inverts an empty dictionary."""
def test_invert_empty_dictionary():
    empty_dict = {}
    assert invert(empty_dict) == {}

"""Invert Use Case: Test if the function inverts a normal dictionary."""
def test_invert_normal_dict_1():
    norm_invert = {"hi": "nya", "yea": "nupur"}
    assert invert(norm_invert) == {"nya" : "hi", "nupur" : "yea"}

"""Invert Use Case: Test if the function inverts another normal dictionary."""
def test_invert_normal_dict_2():
    norm_invert_2 = {"comp110": "hard", "nocomp": "easy"}
    assert invert(norm_invert_2) == {"hard": "comp110", "easy": "nocomp"}

from exercises.ex06.dictionary import favorite_color

"""Favorite_color Edge Case: Test if the function determines the most frequent color when they are all mentioned an equal amount of times."""
def test_favorite_color_equal_dict():
    equal_dict = {"nya": "blue", "david": "red", "jadyn": "orange"}
    assert favorite_color(equal_dict) == "blue"

"""Favorite_color Use Case: Test if the function determines the most frequent color in a normal dictionary."""
def test_favorite_color_normal_color_dict():
    norm_dict = {"nya": "blue", "david": "blue", "jadyn": "red"}
    assert favorite_color(norm_dict) == "blue"

"""Favorite_color Use Case: Test if the function determines the most frequent color in a short dictionary."""
def test_favorite_color_normal_color_2():
    norm_dict_2 = {"caroline": "blue", "david": "blue"}
    assert favorite_color(norm_dict_2) == "blue"

from exercises.ex06.dictionary import count

"""Count Edge Case: Test how the function responds if one of the strings is a number"""
def test_count_num_count():
    edge_count = ["nya", 1, "david", "david"]
    assert count(edge_count) == {'nya': 1, 1: 1, 'david': 2}

"""Count Use Case: Test if the function returns a dictionary corresponding with the number of times a word frequents a given list."""
def test_count_use_count():
    use_count_1 = ["nya", "david", "jadyn", "nya", "nya", "jadyn"]
    assert count(use_count_1) == {"nya": 3, "david": 1, "jadyn": 2}

"""Count Use Case: Test if the function returns a dictionary corresponding with the number of times a word frequents another list."""
def test_count_use_count_2():
    use_count_2 = ["vanilla", "vanilla", "strawberry", "chocolate"]
    assert count(use_count_2) == {"vanilla": 2, "strawberry": 1, "chocolate": 1}

from exercises.ex06.dictionary import alphabetizer

"""Alphebetizer Edge Case: Test if the function returns a dictionary if there is a duplicate"""
def test_alphabetizer_1():
    edge_alphabetizer = ["golden", "golden", "mushroom"]
    assert alphabetizer(edge_alphabetizer) == {"g": ["golden", "golden"], "m": ["mushroom"]}

"""Alphebetizer Use Case: Test a list of animals"""
def test_alphabetizer_2():
    use_alphabetizer = ["cats", "cats", "dogs", "pigs"]
    assert alphabetizer(use_alphabetizer) == {"c": ["cats", "cats"], "d": ["dogs"], "p": ["pigs"]}

"""Alphebetizer Use Case: Test a list of ingredients"""
def test_alphabetizer_3():
    use_alphabetizer_2 = ["salmon", "honey", "mustard", "salt"]
    assert alphabetizer(use_alphabetizer_2) == {"h": ["honey"], "m": ["mustard"], "s": ["salmon", "salt"]}

from exercises.ex06.dictionary import update_attendance

"""Update_attendance Edge Case: Test where the person was already in the attendance roster for that day"""
def test_update_attendance_1():
    attendance_log = {"monday": ["john", "sarah", "mike"]}
    assert update_attendance(attendance_log, "monday", "john") == {"monday": ["john", "sarah", "mike", "john"]}

"""Update_attendance Use Case: Update a normal attendance list"""
def test_update_attendance_2():
    attendance_log = {"monday": ["natalie", "jimmy", "sarah"]}
    assert update_attendance(attendance_log, "monday", "john") == {"monday": ["natalie", "jimmy", "sarah", "john"]}

"""Update_attendance Use Case: Update the attendance list across Monday and Tuesday"""
def test_update_attendance_3():
    attendance_log = {"monday": ["john", "sarah", "mike"], "tuesday": ["jack", "john", "sarah"]}
    assert update_attendance(attendance_log, "monday", "jose") == {"monday": ["john", "sarah", "mike", "jose"], "tuesday": ["jack", "john", "sarah"]}