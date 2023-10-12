"""Practicing function definitions and calling syntax"""

x: int = 1
y: int = 10

def my_max(num1: int, num2: int) -> int:
    """Returns the maximum value out of two numbers"""
    if num1 >= num2:
        return num1
    else: #number1 < number2
        return num2
    
max: int = my_max(x,y)