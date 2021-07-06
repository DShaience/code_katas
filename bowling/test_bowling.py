import unittest
from bowling_classes import Bowling, FrameTypes, Frame, Player
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

    @parameterized.expand([
        [[Frame([3, 4], FrameTypes.NormalFrame)], 0, 7],
        [[Frame([5, 5], FrameTypes.Spare), Frame([3, 8], FrameTypes.NormalFrame), Frame([3, 4], FrameTypes.NormalFrame)], 0, 13],
        [[Frame([10], FrameTypes.Strike), Frame([5, 5], FrameTypes.Spare), Frame([3, 4], FrameTypes.NormalFrame)], 0, 20],
        [[Frame() for i in range(0, 12)], 11, 0],
    ])
    def test_calc_score(self, frames: List[Frame], frame_idx, expected):
        self.assertEqual(self.game.calc_score(frames, frame_idx), expected)

    @staticmethod
    def _test_frame_type(numbers_stream: List[float], frame_idx):
        test_game = Bowling()
        test_game.random_state.insert_mock_numbers_stream(numbers_stream)
        return test_game.play_frame(frame_idx)

    @parameterized.expand([
        [[0.3, 0.4], 0, Frame([3, 4], FrameTypes.NormalFrame)],
        [[0.6, 0.4], 0, Frame([6, 4], FrameTypes.Spare)],
        [[1.0], 0, Frame([10], FrameTypes.Strike)],
    ])
    @patch.object(np.random, 'RandomState', MockRandomState)
    def test_play_frame(self, numbers_stream, frame_idx, expected):
        self.assertEqual(self._test_frame_type(numbers_stream, frame_idx), expected)

    @parameterized.expand([
        [[Frame([10], frame_type=FrameTypes.Strike)] * Bowling.GAME_NUMBER_FRAMES + [Frame([10], FrameTypes.NormalFrame)] * 2, [30] * Bowling.GAME_NUMBER_FRAMES + [0] * 2],
        [[Frame([5, 5], frame_type=FrameTypes.Spare)] * Bowling.GAME_NUMBER_FRAMES + [Frame([5], FrameTypes.NormalFrame)], [15] * Bowling.GAME_NUMBER_FRAMES + [0]],
        [[Frame([9, 0], frame_type=FrameTypes.NormalFrame)] * Bowling.GAME_NUMBER_FRAMES, [9] * Bowling.GAME_NUMBER_FRAMES]
    ])
    def test_game_scorer(self, frames, expected):
        self.assertEqual(self.game.game_scorer(frames), expected)

    @patch.object(np.random, 'RandomState', MockRandomState)
    def test_play_game(self):
        test_game = Bowling()
        numbers_stream = [0.1, 0.3, 0.4, 0.2, 0.1, 0.7,  # 18
                          0.1, 0.2, 0.3, 0.4, 0.5, 0.5,  # 30
                          1.0, 1.0, 0.5, 0.5, 0.2, 0.2,  # 25 + 20 + 12 + 2 + 2 = 61
                          0.2                            # Total: 18 + 30 + 61 = 91 + 18 = 109
                          ]
        test_game.random_state.insert_mock_numbers_stream(numbers_stream)
        test_game.play_game()
        self.assertEqual(test_game.final_score, 109)

        expected_frame_types = [
            FrameTypes.NormalFrame,
            FrameTypes.NormalFrame,
            FrameTypes.NormalFrame,
            FrameTypes.NormalFrame,
            FrameTypes.NormalFrame,
            FrameTypes.Spare,
            FrameTypes.Strike,
            FrameTypes.Strike,
            FrameTypes.Spare,
            FrameTypes.NormalFrame
        ]

        self.assertEqual([frame.frame_type for frame in test_game.frames], expected_frame_types)
        pass


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_validate_player_skill(self):
        probabilities = [0.1] * (Bowling.NUMBER_OF_PINS + 1)
        self.assertRaises(Exception, Player.validate_player_skill, probabilities)

        probabilities = [0.25] * 4
        self.assertRaises(Exception, Player.validate_player_skill, probabilities)

        probabilities = [0.1] * Bowling.NUMBER_OF_PINS
        self.assertEqual(Player.validate_player_skill(probabilities), probabilities)









