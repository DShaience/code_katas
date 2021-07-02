import unittest
from unittest import TestCase

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


