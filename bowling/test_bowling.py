import unittest
from bowling_class import Bowling, FrameTypes
from parameterized import parameterized
from unittest.mock import patch
import numpy as np
from typing import List


class MockRandomState:
    def __init__(self, mock_seed: int = None):
        self.numbers_stream = []
        self.mock_seed = mock_seed  # unused

    def insert_mock_numbers_stream(self, numbers_stream: List[float]):
        assert len(numbers_stream) > 0, "Numbers set must be 1 or more elements"
        numbers_stream.reverse()
        self.numbers_stream = numbers_stream

    def random_sample(self, n):
        assert n > 0, "Can't sample less than 1 number"
        assert n <= len(self.numbers_stream), "Not enough numbers in predefined numbers_stream"
        sampled_numbers = np.array([self.numbers_stream.pop() for i in range(0, n)])
        return sampled_numbers


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
        self.assertEqual(self.game.throw_ball(probability_input), expected)

    @parameterized.expand([
        [5, 1, 1, FrameTypes.NormalFrame],
        [10, 2, 1, FrameTypes.Spare],
        [10, 1, 1, FrameTypes.Strike],
        [8, 1, 10, FrameTypes.FinalFrame],
        [8, 1, 11, FrameTypes.FinalFrame],
    ])
    def test_calc_frame_type(self, number_of_hit_pins, number_of_throws, frame_idx, expected):
        self.assertEqual(self.game.calc_frame_type(number_of_hit_pins, number_of_throws, frame_idx), expected)

    @staticmethod
    def _test_frame_type(numbers_stream: List[float], frame_idx):
        test_game = Bowling()
        test_game.random_state.insert_mock_numbers_stream(numbers_stream)
        return test_game.play_frame(frame_idx)

    @parameterized.expand([
        [[0.3, 0.4], 1, 7, 2, FrameTypes.NormalFrame],
        [[0.6, 0.4], 1, 10, 2, FrameTypes.Spare],
        [[1.0], 1, 10, 1, FrameTypes.Strike],
    ])
    @patch.object(np.random, 'RandomState', MockRandomState)
    def test_play_frame(self, numbers_stream, frame_idx, pins, number_of_throws, frame_type):
        self.assertEqual(self._test_frame_type(numbers_stream, frame_idx), (pins, number_of_throws, frame_type))







