import random
from typing import List, Tuple


def create_coordinates(grid_width: int, grid_height: int) -> List[Tuple[int, int]]:
    """
    Creates a list of coordinates based on the given grid width and height.

    Args:
        grid_width: An integer specifying the width of the grid.
        grid_height: An integer specifying the height of the grid.

    Returns:
        A list of coordinates represented as tuples (x, y) within the specified grid dimensions.

    Example:
        grid_width = 5
        grid_height = 4
        create_coordinates(grid_width, grid_height)
        # Returns [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3),
        #          (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3)]
    """
    grid = [(x, y) for x in range(grid_width) for y in range(grid_height)]
    return grid


def get_location(coordinates: List[Tuple[int, int]], population: int) -> List[Tuple[int, int]]:
    """
    Randomly selects a specified number of locations from the given list of coordinates.

    Args:
        coordinates: A list of coordinates represented as tuples (x, y).
        population: An integer specifying the number of locations to select.

    Returns:
        A list of randomly selected locations from the given coordinates.

    Example:
        coordinates = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
        population = 3
        get_location(coordinates, population)  # Returns [(0, 0), (2, 2), (3, 3)]
    """
    return random.sample(coordinates, population)


valid_dimensions = False
while not valid_dimensions:
    try:
        x_dimension, y_dimension = input("Please enter the dimensions of your map, like (5, 5): ").split(',')
        x_dimension = int(x_dimension.strip())
        y_dimension = int(y_dimension.strip())
        valid_dimensions = True
    except ValueError:
        print("Please enter dimensions in the correct format, like 5, 5.")

grid = create_coordinates(x_dimension, y_dimension)
player, door, dragon1, dragon2 = get_location(grid, 4)

playing = True
while playing:
    move = input("Please enter your move: ").casefold()
