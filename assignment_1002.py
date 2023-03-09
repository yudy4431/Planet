"""
Student ID: 2020726
Author: Yudy Chen
Date: 03/06/2023
Video Link: 
Honor Statement: I have not given or received any unauthorized assistance on this assignment.
"""


import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from assignment_1001 import Planet


def main():

    DAY = 365000
    SIZE = 8

    # part 1
    planet_name = name_of_planets()
    mercury, venus, earth, mars, jupiter, saturn, uranus, neptune = create_planets()
    planet_lst = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
    result = average_distance(planet_name, planet_lst, DAY)
    df = create_table(SIZE, planet_name, result)
    export_csv(df)
    
    

    # part 2
    # Create Planet objects for Earth, Mercury, Venus, and Mars
    mercury = planet_lst[0]
    venus = planet_lst[1]
    earth = planet_lst[2]
    mars = planet_lst[3]

    # Open a file for writing
    with open('planet_distances.csv', 'w') as f:
        # Write the header row
        f.write('Day,Mercury,Venus,Mars\n')
        # Loop through each day and write the distances to the file
        for day in range(1, 1001):
            mercury_distance = distance(earth, mercury, day)
            venus_distance = distance(earth, venus, day)
            mars_distance = distance(earth, mars, day)
            f.write(f'{day},{mercury_distance},{venus_distance},{mars_distance}\n')

    # Load the data from the file into a Pandas DataFrame
    data = pd.read_csv('planet_distances.csv')
    plot_figure(data)

def plot_figure(data):
    """
    Plot distances from Earth to Mercury, Venus, and Mars over time.

    Args:
    data (pd.DataFrame): DataFrame containing distance data for each planet over time.

    Returns:
    None
    """

    plt.plot(data['Day'], data['Mercury'], label='Mercury')
    plt.plot(data['Day'], data['Venus'], label='Venus')
    plt.plot(data['Day'], data['Mars'], label='Mars')
    plt.xlabel('Day')
    plt.ylabel('Distance from Earth (millions of km)')
    plt.title('Distances from Earth to Mercury, Venus, and Mars')
    plt.legend()

    # Add vertical lines to the plot
    plt.axvline(x=300, color='black', linestyle='--')
    plt.axvline(x=600, color='black', linestyle='--')
    plt.axvline(x=900, color='black', linestyle='--')

    plt.show()

def export_csv(df):
    """
    Export a pandas DataFrame to a CSV file.

    Args:
    df (pd.DataFrame): DataFrame to be exported.

    Returns:
    None
    """
    # determining the name of the file
    file_name = '8.csv'
    # saving the excel
    df.to_csv(file_name)

    print('DataFrame is written to CSV File successfully.')

def name_of_planets():
    """
    Return a list of planet names.

    Args:
    None

    Returns:
    list: A list of planet names.
    """
    return ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']

def create_planets():
    """
    Create instances of each planet.

    Args:
    None

    Returns:
    tuple: A tuple containing instances of each planet.
    """

    mercury = Planet(3.5, 88)
    venus = Planet(6.7, 225)
    earth = Planet(9.3, 365)
    mars = Planet(14.2, 687)
    jupiter = Planet(48.4, 4333)
    saturn = Planet(88.9, 10759)
    uranus = Planet(179, 30687)
    neptune = Planet(288, 60190)

    return mercury, venus, earth, mars, jupiter, saturn, uranus, neptune

def create_table(table_size, planet_name, distance_result):
    """
    Creates a table of distances between planets using a 2-dimensional numpy array.

    Args:
    - table_size: An integer indicating the number of planets to include in the table.
    - planet_name: A list of strings representing the names of the planets.
    - distance_result: A dictionary of distances between pairs of planets.

    Returns:
    - A Pandas DataFrame containing the distances between each pair of planets.
    """
    # Create a 2-dimensional numpy array of zeros with dimensions given.
    dist_arr = np.zeros((table_size, table_size))

    # Iterate over the rows and columns of dist_arr
    for i in range(table_size):
        for j in range(i+1, table_size):
            # Get the planet names for the current row and column
            planet1 = planet_name[i]
            planet2 = planet_name[j]
            # Assign the corresponding value from result to the current element of dist_arr
            dist_arr[i, j] = distance_result[(planet1, planet2)]
            dist_arr[j, i] = distance_result[(planet1, planet2)]

    # Create a DataFrame from the numpy array
    df = pd.DataFrame(dist_arr, columns=planet_name, index=planet_name)

    return df

def average_distance(planet_name, planet_lst, day):
    """
    Calculates the average distance between each pair of planets for a given number of days.

    Args:
    - planet_name: A list of strings representing the names of the planets.
    - planet_lst: A list of Planet objects representing the planets in the solar system.
    - day: An integer indicating the number of days to calculate the distance for.

    Returns:
    - A dictionary containing the average distance between each pair of planets.
    """

    planet_dic = {}
    result = {}

    for i, planet1 in enumerate(planet_lst):
        
        for j, planet2 in enumerate(planet_lst[i+1:]):

            planet_dic[(planet1, planet2)] = []

            for ele in range(day):

                d = distance(planet1, planet2, ele)
                planet_dic[(planet1,planet2)].append(d)

            avg_distance = sum(planet_dic[(planet1, planet2)]) / len(planet_dic[(planet1, planet2)])

            result[(planet_name[i], planet_name[i+1:][j])] = round(avg_distance, 2)
    
    return result

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
