import random
import unittest

from helpers.enums import Direction
from helpers.funcs import move_player, move_dragon


class TestMovePlayer(unittest.TestCase):

    def test_move_player_up(self):
        player = (2, 3)
        direction = Direction.UP
        expected_result = (2, 2)
        self.assertEqual(move_player(player, direction), expected_result)

    def test_move_player_down(self):
        player = (2, 3)
        direction = Direction.DOWN
        expected_result = (2, 4)
        self.assertEqual(move_player(player, direction), expected_result)

    def test_move_player_left(self):
        player = (2, 3)
        direction = Direction.LEFT
        expected_result = (1, 3)
        self.assertEqual(move_player(player, direction), expected_result)

    def test_move_player_right(self):
        player = (2, 3)
        direction = Direction.RIGHT
        expected_result = (3, 3)
        self.assertEqual(move_player(player, direction), expected_result)


class TestMoveDragon(unittest.TestCase):

    def test_move_dragon_avoid_other_dragon(self):
        dragon = (3, 3)
        other_dragon = (2, 3)
        player = (2, 2)
        valid_positions = [(2, 3), (3, 2), (4, 3), (3, 4)]
        random.seed(0)  # Set seed for deterministic testing
        new_position = move_dragon(dragon, other_dragon, player, valid_positions)
        self.assertNotEqual(new_position, other_dragon)  # The dragon should not move to the other dragon's position


if __name__ == '__main__':
    unittest.main()
