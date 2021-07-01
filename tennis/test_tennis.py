import unittest
from tennis_game_class import Tennis
from parameterized import parameterized


class TestStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Tennis()

    @parameterized.expand([
        [0, 4, True],
        [1, 4, True],
        [2, 3, False],
        [4, 3, False],
    ])
    def test_is_victory(self, score_1, score_2, expected):
        self.assertEqual(self.game.is_victory(score_1, score_2), expected)




