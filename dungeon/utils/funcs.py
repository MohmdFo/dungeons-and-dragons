import os
import random
from typing import List

from dungeon.helpers.enums import Direction
from dungeon.helpers.types import (
    Position,
    Coordinates
)


def get_moves(player: Position, max_coordinate: int) -> List[Direction]:
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


def move_player(player: Position, direction: Direction) -> Position:
    """
    Moves the player in the specified direction.

    Args:
        player: A tuple representing the current player position as (x, y).
        direction: The direction in which the player should move
                   (one of the Direction enum values).

    Returns:
        A tuple representing the new player position after the move as (new_x, new_y).

    Example:
        player = (2, 3)
        direction = Direction.UP
        move_player(player, direction)
        # Returns (2, 2)

    Note:
        Assumes that the grid is represented with the origin
        (0, 0)in the top-left corner.
        Moving "up" decreases the y-coordinate, moving "down"
        increases the y-coordinate,
        moving "left" decreases the x-coordinate, and moving
        "right" increases the x-coordinate.
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


def draw_map(grid_width: int, grid_height: int, player: Position) -> None:
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
            # elif (x, y) == door:
            #     print('D', end=' ')
            # elif (x, y) == dragon1 or (x, y) == dragon2:
            #     print('E', end=' ')
            else:
                print('_', end=' ')
        print()


def create_coordinates(grid_width: int, grid_height: int) -> Coordinates:
    """
    Creates a list of coordinates based on the given grid width and height.

    Args:
        grid_width: An integer specifying the width of the grid.
        grid_height: An integer specifying the height of the grid.

    Returns:
        A list of coordinates represented as tuples (x, y)
        within the specified grid dimensions.

    Example:
        grid_width = 5
        grid_height = 4
        create_coordinates(grid_width, grid_height)
        # Returns [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3),
        # (2, 0), (2, 1), (2, 2), (2, 3),
        #          (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3)]
    """
    grid = [(x, y) for x in range(grid_width) for y in range(grid_height)]
    return grid


def get_location(coordinates: Coordinates, population: int) -> Coordinates:
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


def get_valid_positions(grid: Coordinates, player: Position, door: Position) -> Coordinates: # noqa E501
    """
    Returns a list of all valid positions for a dragon.

    Args:
        grid: A list of all positions within the grid.
        player: The current position of the player.
        door: The current position of the door.

    Returns:
        A list of tuples representing valid positions for a dragon.
    """
    valid_positions = [pos for pos in grid if pos != player and pos != door]
    return valid_positions


def move_dragon(dragon: Position, other_dragon: Position, player: Position, valid_positions: Coordinates) -> Position:
    """
    Moves the dragon to a new random position from the list of valid positions
    with a 50% probability. If the player is within 3 squares of distance,
    the dragon also has a 50% chance of moving towards the player.

    Args:
        dragon: The current position of the dragon.
        other_dragon: The current position of the other dragon.
        player: The current position of the player.
        valid_positions: A list of tuples representing valid positions for a dragon.

    Returns:
        A tuple representing the new position of the dragon.
    """
    # Remove the other dragon's position from the list of valid positions
    valid_positions = [pos for pos in valid_positions if pos != other_dragon]

    # Calculate the Euclidean distance between the dragon and the player
    distance_to_player = ((player[0] - dragon[0]) ** 2 + (player[1] - dragon[1]) ** 2) ** 0.5

    # Determine the probability of moving - it's 50% in all cases now
    probability_of_moving = 0.5

    # Check if the dragon will move
    if random.random() < probability_of_moving:
        # If the dragon is moving towards the player, select a valid position closer to the player
        if distance_to_player <= 3:
            valid_positions = [pos for pos in valid_positions if ((pos[0] - player[0]) ** 2 + (pos[1] - player[1]) ** 2) ** 0.5 <= distance_to_player]
            # If there are no valid positions closer to the player, use all valid positions
            if not valid_positions:
                valid_positions = [pos for pos in valid_positions if pos != other_dragon]

        # If there are valid positions, choose one randomly
        if valid_positions:
            dragon = random.choice(valid_positions)
    return dragon


def is_player_near_dragon(player: Position, dragon1: Position, dragon2: Position) -> bool:
    """
    Calculates the distance between the player and the dragons,
    and returns True if the distance is 1 for either dragon.

    Args:
        player: A tuple representing the player's position (x, y).
        dragon1: A tuple representing the first dragon's position (x, y).
        dragon2: A tuple representing the second dragon's position (x, y).

    Returns:
        A boolean value indicating if the player is near either dragon.

    Example:
        player = (2, 3)
        dragon1 = (3, 3)
        dragon2 = (2, 4)
        is_player_near_dragon(player, dragon1, dragon2)  # Returns True
    """
    distance_to_dragon1 = ((player[0] - dragon1[0]) ** 2 + (player[1] - dragon1[1]) ** 2) ** 0.5
    distance_to_dragon2 = ((player[0] - dragon2[0]) ** 2 + (player[1] - dragon2[1]) ** 2) ** 0.5
    result = distance_to_dragon1 == 1 or distance_to_dragon2 == 1
    return result
