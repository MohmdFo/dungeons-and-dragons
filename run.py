import random


def create_coordinations(grid_width: int, grid_height: int) -> list[tuple[int, int], tuple[int, int]]:
    grid = [(x, y) for x in range(grid_width) for y in range(grid_height)]
    return grid


def get_location(coordinates: list, population: int):
    return random.sample(coordinates, population)

grid = create_coordinations(5, 5)

player, door, dragon1, dragon2 = get_location(grid, 4)

playing = True
while playing:
    move = input("please enter your move: ").casefold()