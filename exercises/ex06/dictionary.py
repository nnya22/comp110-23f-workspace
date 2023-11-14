"""Getting some practice with dictionary functions!"""

__author__ = "730324119"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values."""
    new_dict: dict[str, str] = {}
    for key_1 in input:
        for key_2 in new_dict:
            if key_2 == input[key_1]:
                raise KeyError("You cannot have two values that are the same!")
        new_dict[input[key_1]] = key_1
    return new_dict


def favorite_color(input: dict[str, str]) -> str:
    """Return the color that appears most frequently."""
    colors: dict[str, int] = {}
    favorite_color: str = ""
    for key in input:
        if input[key] not in colors:
            colors[input[key]] = 0
        colors[input[key]] += 1
        if favorite_color == "":
            favorite_color = input[key]
        else:
            if colors[input[key]] > colors[favorite_color]:
                favorite_color = input[key]
    return favorite_color


def count(input: list[str]) -> dict[str, int]:
    """Count instances of string in list."""
    counts: dict[str, int] = {}
    for item in input:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1
    return counts


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Sort list into dictionary based on first letter."""
    alphabet_list: dict[str, list[str]] = {}
    for item in input:
        first_letter = item[0].lower()
        if first_letter not in alphabet_list:
            alphabet_list[first_letter] = []
        alphabet_list[first_letter].append(item)
    return alphabet_list


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Update attendance list with new day and student."""
    if day not in input:
        input[day] = []
    input[day].append(student)
    return input