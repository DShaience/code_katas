import bisect
from typing import List
from enum import Enum
import numpy as np
from math import isclose
from tabulate import tabulate


class FrameTypes(Enum):
    NormalFrame = 0
    Spare = 1
    Strike = 2


class Frame:
    def __init__(self, pins_round_list=None, frame_type=None):
        if pins_round_list is None:
            self.round: list = []
        else:
            self.round: list = pins_round_list
        self.frame_type = frame_type

    def __eq__(self, other):
        if isinstance(other, Frame):
            return (self.round == other.round) and (self.frame_type == other.frame_type)
        return False


class Player:
    def __init__(self, pins_hit_probability: List[float] = None, name: str = 'Default Player'):
        """
        :param pins_hit_probability: the probability of hitting each pin. I.e., [probability of 0 pins, of 1, of 2, ..., of 10]
        """
        if pins_hit_probability is None:
            pins_hit_probability = self._uniform_probability()
        self.pins_hit_probability = self.validate_player_skill_array(pins_hit_probability)
        self.cumulative_probability = self.map_pins_hit_probability_to_cumulative_probability(self.pins_hit_probability)
        self.name = name

    @staticmethod
    def _uniform_probability():
        return [0.1] * Bowling.NUMBER_OF_PINS

    @staticmethod
    def validate_player_skill_array(pins_hit_probability):
        probability_sum = sum(pins_hit_probability)
        if not isclose(probability_sum, 1.0, rel_tol=0.0000001):
            raise Exception(f"Probability must add-up to 1.0, but instead got: {probability_sum}")
        if len(pins_hit_probability) != Bowling.NUMBER_OF_PINS:
            raise Exception(f"The number of probabilities should be equal to the number of pins. Got {len(pins_hit_probability)} instead.")
        if any([proba == 0.0 for proba in pins_hit_probability]):
            raise Exception(f"All pins must have non-zero probability, even if very small")
        return pins_hit_probability

    @staticmethod
    def throw_ball(cumulative_probability, throw_probability: float, verbose: bool = False):
        assert 0.0 <= throw_probability <= 1.0, f"Throw probability must be a probability, i.e., a number between [0. 1]. got {throw_probability} instead."
        number_of_hit_pins = bisect.bisect_left(cumulative_probability, throw_probability)
        if verbose:
            print(number_of_hit_pins)
        return number_of_hit_pins

    @staticmethod
    def map_pins_hit_probability_to_cumulative_probability(pins_hit_probability) -> np.array:
        cumulative_proba = np.cumsum(pins_hit_probability)
        cumulative_proba_padded = np.insert(cumulative_proba, 0, 0.0)
        cumulative_proba_normalized = (cumulative_proba_padded - np.min(cumulative_proba_padded)) / (np.max(cumulative_proba_padded) - np.min(cumulative_proba_padded))
        return cumulative_proba_normalized


class Bowling:
    GAME_NUMBER_FRAMES = 10
    NUMBER_OF_PINS = 10

    def __init__(self, player: Player, seed=12345):
        self.random_state = np.random.RandomState(seed)
        self.scores = [np.nan] * (self.GAME_NUMBER_FRAMES + 2)
        self.final_score = 0
        self.frames: List[Frame] = []
        self.player = player

    @staticmethod
    def calc_spare_score(frames: List[Frame], frame_idx):
        return sum(frames[frame_idx].round) + frames[frame_idx+1].round[0]

    @staticmethod
    def calc_strike_score(frames: List[Frame], frame_idx):
        score = sum(frames[frame_idx].round) + sum(frames[frame_idx+1].round)
        if len(frames[frame_idx+1].round) == 1:
            score += frames[frame_idx+2].round[0]
        return score

    @staticmethod
    def calc_normal_score(frame: Frame):
        return sum(frame.round)

    def calc_score(self, frames: List[Frame], frame_idx):
        if frame_idx >= self.GAME_NUMBER_FRAMES:
            return 0
        if frames[frame_idx].frame_type == FrameTypes.NormalFrame:
            return self.calc_normal_score(frames[frame_idx])
        elif frames[frame_idx].frame_type == FrameTypes.Spare:
            return self.calc_spare_score(frames, frame_idx)
        else:
            return self.calc_strike_score(frames, frame_idx)

    def throw_ball(self, cumulative_probability, throw_probability: float, verbose: bool = False):
        return self.player.throw_ball(cumulative_probability, throw_probability, verbose)

    def calc_frame_type(self, number_of_hit_pins: int, number_of_throws: int, frame_idx: int):
        if frame_idx >= self.GAME_NUMBER_FRAMES:
            return FrameTypes.NormalFrame
        elif number_of_hit_pins < self.NUMBER_OF_PINS:
            return FrameTypes.NormalFrame
        elif number_of_throws == 2:
            return FrameTypes.Spare
        else:
            return FrameTypes.Strike

    def play_frame(self, frame_idx: int):
        pins_round = []
        pins = self.throw_ball(self.player.cumulative_probability, self.random_state.random_sample(1)[0])
        pins_round.append(pins)
        if pins < self.NUMBER_OF_PINS:
            next_throw_pins = min([self.NUMBER_OF_PINS - pins, self.throw_ball(self.player.cumulative_probability, self.random_state.random_sample(1)[0])])
            pins_round.append(next_throw_pins)

        frame_type = self.calc_frame_type(sum(pins_round), len(pins_round), frame_idx)
        frame = Frame(pins_round, frame_type)
        return frame

    def game_scorer(self, frames: List[Frame]):
        frame_scores = []
        for frame_idx in range(0, len(frames)):
            frame_scores.append(self.calc_score(frames, frame_idx))
        return frame_scores

    def print_game_results(self):
        frame_type_representation = {
            FrameTypes.NormalFrame: "",
            FrameTypes.Spare: "/",
            FrameTypes.Strike: "X"
        }
        print(f"Player: {self.player.name}")
        headers = ['Frame', 'Pins hit', 'Frame type', 'Frame score']
        frames_info = []
        for i, frame in enumerate(self.frames):
            frames_info.append([i+1, frame.round, frame_type_representation[frame.frame_type], self.scores[i]])
        print(tabulate([headers] + frames_info, numalign='center', stralign='center'))
        print(f"Final score: {self.final_score}")

    def play_game(self):
        for frame_idx in range(0, self.GAME_NUMBER_FRAMES):
            frame = self.play_frame(frame_idx)
            self.frames.append(frame)

        additional_throws_to_play_map = {
            FrameTypes.NormalFrame: 0,
            FrameTypes.Spare: 1,
            FrameTypes.Strike: 2
        }

        additional_throws_to_play = additional_throws_to_play_map[self.frames[-1].frame_type]
        if additional_throws_to_play > 0:
            final_frame = self.play_frame(self.GAME_NUMBER_FRAMES)
            final_frame.round = final_frame.round[0: additional_throws_to_play]
            self.frames.append(final_frame)

        self.scores = self.game_scorer(self.frames)
        self.final_score = sum(self.scores)


if __name__ == '__main__':
    my_player = Player(name='Bruce Willis')
    my_game = Bowling(my_player, 12345)
    my_game.play_game()
    my_game.print_game_results()
