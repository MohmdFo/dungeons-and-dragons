import os
import random
from typing import List, Tuple

from .enums import Direction


def get_moves(player: Tuple[int, int], max_coordinate: int) -> List[Direction]:
    """
    Retrieves the available moves for the player within the given grid dimensions.

    Args:
        player: A tuple representing the current player position (x, y).
        max_coordinate: An integer specifying the maximum coordinate value in the grid.

    Returns:
        A list of available moves as Direction enum values.

    Example:
        player = (2, 2)
        max_coordinate = 5
        get_moves(player, max_coordinate)
        # Returns [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
    """
    moves = list(Direction)
    x, y = player

    if x == 0:
        moves.remove(Direction.LEFT)
    if x == max_coordinate - 1:
        moves.remove(Direction.RIGHT)
    if y == 0:
        moves.remove(Direction.UP)
    if y == max_coordinate - 1:
        moves.remove(Direction.DOWN)

    return moves


def clear_screen() -> int:
    """
    Clears the console screen.

    Returns:
        The exit status of the clear screen command.

    Example:
        clear_screen()  # Clears the console screen.
    """
    return os.system('cls' if os.name == 'nt' else 'clear')


def move_player(player: Tuple[int, int], direction: Direction) -> Tuple[int, int]:
    """
    Moves the player in the specified direction.

    Args:
        player: A tuple representing the current player position as (x, y).
        direction: The direction in which the player should move (one of the Direction enum values).

    Returns:
        A tuple representing the new player position after the move as (new_x, new_y).

    Example:
        player = (2, 3)
        direction = Direction.UP
        move_player(player, direction)
        # Returns (2, 2)

    Note:
        Assumes that the grid is represented with the origin (0, 0) in the top-left corner.
        Moving "up" decreases the y-coordinate, moving "down" increases the y-coordinate,
        moving "left" decreases the x-coordinate, and moving "right" increases the x-coordinate.
    """
    x, y = player

    if direction == Direction.UP:
        y -= 1
    if direction == Direction.DOWN:
        y += 1
    if direction == Direction.LEFT:
        x -= 1
    if direction == Direction.RIGHT:
        x += 1

    return x, y


def draw_map(grid_width: int, grid_height: int, player: Tuple[int, int]) -> None:
    """
    Prints a grid map of the game.

    Args:
        grid_width: An integer specifying the width of the grid.
        grid_height: An integer specifying the height of the grid.
        player: The coordinates of the player, represented as a tuple (x, y).
    
    Returns:
        None.
    """
    for y in range(grid_height):
        for x in range(grid_width):
            if (x, y) == player:
                print('X', end=' ')
            else:
                print('_', end=' ')
        print()


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
