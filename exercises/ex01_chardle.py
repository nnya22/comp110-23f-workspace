"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730324119"

five_c: str = input("Enter a 5-character word: ")
single_c: str = input("Enter a single character: ")

print("Searching for " + single_c + " in " + five_c)

instances: int = 0 

if five_c[0] == single_c:
    print(single_c + " found at index 0")
    instances: int = 1
else:
    instances: int = 0  
    if five_c[1] == single_c:
        print(single_c + " found at index 1")
        instances: int = 1 + 1
    else:
        instances: int = 0
if five_c[2] == single_c:
    print(single_c + " found at index 2")
if five_c[3] == single_c:
    print(single_c + " found at index 3")
if five_c[4] == single_c:
    print(single_c + " found at index 4")



if     
    print( + "instances of" + single_c + "found in" + five_c) 
else:
    print("No instances of" + single_c + "found in" + five_c)