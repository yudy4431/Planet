"""
Student ID: 2020726
Author: Yudy Chen
Date: 03/06/2023
Video Link: 
Honor Statement: I have not given or received any unauthorized assistance on this assignment.
"""


import math

class Planet:
    """
    A class representing a planet.

    Attributes:
    - radius: the average distance from the planet to its center in millions of kilometers
    - year: the number of Earth days it takes for the planet to complete one orbit around the sun
    """

    def __init__(self, radius, year):
        """
        Initialize a Planet object.

        Parameters:
        - radius: the average distance from the planet to its center in millions of kilometers
        - year: the number of Earth days it takes for the planet to complete one orbit around the sun
        """

        self.radius = radius
        self.year = year

    def position(self, day):
        """
        Calculate the position of the planet on a specific day.

        Parameters:
        - day: the number of Earth days since the planet's last perihelion passage

        Returns:
        - a tuple representing the x and y coordinates of the planet relative to the sun
        """

        theta = (2 * math.pi * day) / self.year
        x = self.radius * math.cos(theta)
        y = self.radius * math.sin(theta)

        return round(x, 2), round(y, 2)


def main():

    mercury = Planet(3.5, 88)
    print(mercury.position(0))
    print(mercury.position(22))		
    print(mercury.position(33))	
    print(mercury.position(440))

    earth = Planet(9.3, 365)
    mars = Planet(14.2, 687)

    d = distance(earth, mars, 732)	
    
    print(f"{d} million miles")


def distance(planet1, planet2, day):
    """
    Calculate the distance between two planets on a specific day.

    Parameters:
    - planet1: a Planet object representing the first planet
    - planet2: a Planet object representing the second planet
    - day: the number of Earth days since the planets' last perihelion passage

    Returns:
    - the distance between the two planets in millions of kilometers, rounded to two decimal places
    """

    x1, y1 = planet1.position(day)
    x2, y2 = planet2.position(day)

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return round(distance, 2)

if __name__ == '__main__':
    main()
