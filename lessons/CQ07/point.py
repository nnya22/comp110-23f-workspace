from __future__ import annotations

"""Lesson exploring OOP (Object Oriented Programming)!"""
__author__ = "730324119"


class Point:
    """A new class that has both an x and a y attribute!"""
    x: float
    y: float
    
    def __init__(self, x_init: float, y_init: float):
        """My constructor!"""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """A method that belongs to the Point class and mutates a Point!"""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """A method that belongs to the Point class and instead of mutating a Point, it creates a new Point!"""
        update_x = self.x * factor
        update_y = self.y * factor
        return Point(update_x, update_y)
    


        


    
