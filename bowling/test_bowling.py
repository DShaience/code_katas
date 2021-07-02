import unittest
from bowling_class import Bowling
from parameterized import parameterized


class TestBowling(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Bowling()

    @parameterized.expand([
        [10, True],
        [9, False],
        [11, False],
    ])
    def test_is_final_frame(self, frame, expected):
        self.assertEqual(self.game.is_final_frame(frame), expected)

    @parameterized.expand([
        [[10, 10], 20],
        [[1], 1],
        [[], 0],
    ])
    def test_calc_strike_score(self, last_frames, expected):
        self.assertEqual(self.game.calc_strike_score(last_frames), expected)

    @parameterized.expand([
        [[10], 10],
        [[1], 1],
        [[], 0],
        [[0], 0],
    ])
    def test_calc_spare_score(self, last_frames, expected):
        self.assertEqual(self.game.calc_spare_score(last_frames), expected)

    @parameterized.expand([
        [0.0, 0],
        [0.2, 2],
        [0.33, 3],
        [0.46, 5],
        [1.0, 10],
    ])
    def test_throw_ball(self, probability_input, expected):
        self.assertEquals(self.game.throw_ball(probability_input), expected)










