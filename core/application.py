import logging

from conf import *
from dungeon.helpers.enums import Direction
from dungeon.helpers.const import (
    RUNNING,
    EXIT_COMMANDS,
)
from dungeon.utils.funcs import (
    draw_map,
    get_moves,
    move_dragon,
    move_player,
    clear_screen,
    get_location,
    create_coordinates,
    get_valid_positions,
    is_player_near_dragon
)


logger = logging.getLogger(__name__)


def app():
    valid_dimensions = False
    while not valid_dimensions:
        try:
            x_dimension, y_dimension = input("Please enter the dimensions of your map, like (5, 5): ").split(',') # noqa E501
            x_dimension = int(x_dimension.strip())
            y_dimension = int(y_dimension.strip())
            valid_dimensions = True
            continue
        except ValueError:
            print("Please enter dimensions in the correct format, like 5, 5.")

    grid = create_coordinates(x_dimension, y_dimension)
    player, door, dragon1, dragon2 = get_location(grid, 4)

    while RUNNING:
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
            valid_positions = get_valid_positions(grid, player, door)
            dragon1 = move_dragon(dragon1, dragon2, player, valid_positions)
            dragon2 = move_dragon(dragon2, dragon1, player, valid_positions)
            if player == dragon1 or player == dragon2:
                print("You lost the game!")
                break
            elif is_player_near_dragon(player, dragon1, dragon2):
                print("You lost the game! Dragon saw you")
                break
            elif player == door:
                print("You won the game!")
                break
            clear_screen()
        else:
            print("Please enter a valid move.")
            clear_screen()
