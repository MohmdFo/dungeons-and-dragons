import random
from enum import Enum
from typing import List, Tuple


class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


def get_moves(player, max_coordinate):
    moves = list(Direction)
    x, y = player

    if x == 0:
        moves.remove(Direction.LEFT)
    if x == max_coordinate:
        moves.remove(Direction.RIGHT)
    if y == 0:
        moves.remove(Direction.UP)
    if y == max_coordinate:
        moves.remove(Direction.DOWN)

    return moves


def move_player(player, direction):
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
    valid_moves = get_moves(player, x_dimension)
    draw_map(x_dimension, y_dimension, player)
    print(f"You are in room: {player}")
    print(f"You can move in: {', '.join([move.value for move in valid_moves])}")
    direction_input = input("Please enter your move: ").casefold()

    try:
        direction = Direction(direction_input)
    except ValueError:
        print("Please enter a valid direction: up, down, left, or right.")
        continue

    if direction in valid_moves:
        player = move_player(player, direction)
        if player == dragon1 or player == dragon2:
            print("You lost the game!")
            break
        if player == door:
            print("You won the game!")
            break
    else:
        print("Please enter a valid move.")
