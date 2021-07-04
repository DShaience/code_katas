import unittest
from bowling_class import Bowling, FrameTypes, Frame
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
        [8, 1, 10, FrameTypes.NormalFrame],
        [8, 1, 11, FrameTypes.NormalFrame],
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

    @parameterized.expand([
        [0, FrameTypes.NormalFrame, True],
        [4, FrameTypes.Spare, True],
        [4, FrameTypes.Strike, True],
        [9, FrameTypes.NormalFrame, False],
        [9, FrameTypes.Spare, True],
        [10, FrameTypes.Spare, True],
        [10, FrameTypes.Strike, True],
        [11, FrameTypes.Strike, True],
    ])
    def test_continue_game_indicator(self, frame_idx, pre_final_frame_type, expected):
        self.assertEqual(self.game.continue_game_indicator(frame_idx, pre_final_frame_type), expected)

    @parameterized.expand([
        [Frame([2, 6]), 8],
        [Frame([3, 4]), 7],
    ])
    def test_calc_normal_score(self, frame: Frame, expected):
        self.assertEqual(self.game.calc_normal_score(frame), expected)

    @parameterized.expand([
        [[Frame([5, 5]), Frame([5, 5])], 0, 15],
        [[Frame([3, 7]), Frame([2, 7])], 0, 12],
    ])
    def test_calc_spare_score(self, frames: List[Frame], frame_idx, expected):
        self.assertEqual(self.game.calc_spare_score(frames, frame_idx), expected)

    @parameterized.expand([
        [[Frame([10]), Frame([5, 5]), Frame([5, 5])], 0, 20],
        [[Frame([10]), Frame([10]), Frame([5, 5])], 0, 25],
    ])
    def test_calc_strike_score(self, frames: List[Frame], frame_idx, expected):
        self.assertEqual(self.game.calc_strike_score(frames, frame_idx), expected)


        # def calc_strike_score(frames: List[Frame], frame_idx):

    #


    # fixme: fix this test
    # @parameterized.expand([
    #     [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10], 1, FrameTypes.NormalFrame, 2],
    #     [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10], 9, FrameTypes.Spare, 20],
    #     [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10], 9, FrameTypes.Strike, 30],
    # ])
    # def test_calc_score(self, pins, frame_idx, frame_type, expected):
    #     self.assertEqual(self.game.calc_score(pins, frame_idx, frame_type), expected)

    # @parameterized.expand([
        # [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9],
        #  [FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame,
        #   FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame,
        #   FrameTypes.NormalFrame, FrameTypes.NormalFrame],
        #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0]
        #  ],

        # [[0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 10, 9],
        #  [FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame,
        #   FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.Spare,
        #   FrameTypes.NormalFrame, FrameTypes.NormalFrame],
        #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 20, 0, 0]
        #  ],
        #
        # [[0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 10, 9],
        #  [FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame,
        #   FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.Strike,
        #   FrameTypes.NormalFrame, FrameTypes.NormalFrame],
        #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 29, 0, 0]
        #  ],
        #
        # [[0, 1, 2, 3, 10, 5, 6, 7, 8, 9, np.nan, np.nan],
        #  [FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.Strike,
        #   FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame, FrameTypes.NormalFrame],
        #  [0, 1, 2, 3, 21, 5, 6, 7, 8, 9]
        #  ],
        #
        # [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        #  [FrameTypes.Strike, FrameTypes.Strike, FrameTypes.Strike, FrameTypes.Strike, FrameTypes.Strike,
        #   FrameTypes.Strike, FrameTypes.Strike, FrameTypes.Strike, FrameTypes.Strike, FrameTypes.Strike,
        #   FrameTypes.NormalFrame, FrameTypes.NormalFrame],
        #  [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 0, 0]
        #  ],
        #
        # [[5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, np.nan],
        #  [FrameTypes.NormalFrame, FrameTypes.Spare, FrameTypes.NormalFrame, FrameTypes.Spare, FrameTypes.NormalFrame,
        #   FrameTypes.Spare, FrameTypes.NormalFrame, FrameTypes.Spare, FrameTypes.NormalFrame, FrameTypes.Spare,
        #   FrameTypes.NormalFrame],
        #  [5, 15, 5, 15, 5, 15, 5, 15, 5, 15, 0]
        #  ],
        #
        # [[10, 5, 10, 5, 10, 5, 10, 5, 10, 5, np.nan, np.nan],
        #  [FrameTypes.Spare, FrameTypes.NormalFrame, FrameTypes.Spare, FrameTypes.NormalFrame, FrameTypes.Spare,
        #   FrameTypes.NormalFrame, FrameTypes.Spare, FrameTypes.NormalFrame, FrameTypes.Spare, FrameTypes.NormalFrame],
        #  [15, 5, 15, 5, 15, 5, 15, 5, 15, 5]
        #  ],

        # fixme: the all-spare test case should be fixed, along with other spare calculations (see below)
        # [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, np.nan],
        #  [FrameTypes.Spare, FrameTypes.Spare, FrameTypes.Spare, FrameTypes.Spare, FrameTypes.Spare,
        #   FrameTypes.Spare, FrameTypes.Spare, FrameTypes.Spare, FrameTypes.Spare, FrameTypes.Spare,
        #   FrameTypes.NormalFrame
        #   ],
        #  [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 0]
        #  ],
    # ])
    # def test_game_scorer(self, pins, frame_types, expected):
    #     self.assertEqual(self.game.game_scorer(pins, frame_types), expected)
    #     pass

    # fixme: spare and strike score should only take the FIRST throw in the next frame
    #  Currently, this by error, takes into account the ENTIRE next frame
    #  This means that the SEPARATE throws should also be saved to memory and that calc_spare and calc_strike should
    #  use this new array

