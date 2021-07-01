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

    @parameterized.expand([
        [0, 4, False],
        [0, 3, True],
        [2, 3, True],
        [3, 3, False],
        [4, 3, False],
        [4, 5, False],
    ])
    def test_is_simple_game_phase(self, score_1, score_2, expected):
        self.assertEqual(self.game.is_simple_game_phase(score_1, score_2), expected)

    @parameterized.expand([
        [3, 3, True],
        [0, 3, False],
        [4, 3, False],
    ])
    def test_is_deuce(self, score_1, score_2, expected):
        self.assertEqual(self.game.is_deuce(score_1, score_2), expected)

    @parameterized.expand([
        [0, 0, ['Love', 'Love']],
        [0, 1, ['Love', '15']],
        [1, 0, ['15', 'Love']],
        [2, 1, ['30', '15']],
        [3, 2, ['40', '30']],
    ])
    def test__simple_phase_score_translator(self, score_1, score_2, expected):
        self.assertEqual(self.game.simple_phase_score_translator(score_1, score_2), expected)



