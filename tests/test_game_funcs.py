import unittest

from helpers.enums import Direction
from helpers.funcs import (
    get_moves,
    create_coordinates,
    get_location,
    get_valid_positions,
    is_player_near_dragon
)

class TestGameFunctions(unittest.TestCase):

    def test_get_moves(self):
        player = (2, 2)
        max_coordinate = 5
        moves = get_moves(player, max_coordinate)
        self.assertCountEqual(moves, [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT])

        player = (0, 0)
        moves = get_moves(player, max_coordinate)
        self.assertCountEqual(moves, [Direction.DOWN, Direction.RIGHT])

    def test_create_coordinates(self):
        grid_width = 5
        grid_height = 4
        coords = create_coordinates(grid_width, grid_height)
        self.assertCountEqual(coords, [(x, y) for x in range(grid_width) for y in range(grid_height)])

    def test_get_location(self):
        coordinates = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
        population = 3
        locations = get_location(coordinates, population)
        self.assertEqual(len(locations), population)
        for loc in locations:
            self.assertIn(loc, coordinates)

    def test_get_valid_positions(self):
        grid = [(0, 0), (0, 1), (1, 0), (1, 1)]
        player = (0, 0)
        door = (1, 1)
        valid_positions = get_valid_positions(grid, player, door)
        self.assertCountEqual(valid_positions, [(0, 1), (1, 0)])

    def test_is_player_near_dragon(self):
        player = (2, 3)
        dragon1 = (3, 3)
        dragon2 = (2, 4)
        self.assertTrue(is_player_near_dragon(player, dragon1, dragon2))

        player = (2, 2)
        self.assertFalse(is_player_near_dragon(player, dragon1, dragon2))


if __name__ == '__main__':
    unittest.main()
