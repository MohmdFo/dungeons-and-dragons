from helpers.enums import Direction
from helpers.funcs import (
    create_coordinates,
    get_location,
    get_moves,
    draw_map,
    move_player,
    clear_screen,
    get_valid_positions,
    move_dragon,
)


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
        valid_positions = get_valid_positions(grid, player, door)
        dragon1 = move_dragon(dragon1, dragon2, valid_positions)
        dragon2 = move_dragon(dragon2, dragon1, valid_positions)
        if player == dragon1 or player == dragon2:
            print("You lost the game!")
            break
        if player == door:
            print("You won the game!")
            break
        clear_screen()
    else:
        print("Please enter a valid move.")
        clear_screen()
