from typing import List
from enum import Enum
import numpy as np


class FrameTypes(Enum):
    NormalFrame = 0
    Spare = 1
    Strike = 2
    # FinalFrame = 3


class Frame:
    def __init__(self, pins_round_list=None, frame_type=None):
        if pins_round_list is None:
            self.round = []
        else:
            self.round = pins_round_list
        self.frame_type = frame_type


class Bowling:
    GAME_NUMBER_FRAMES = 10
    NUMBER_OF_PINS = 10

    def __init__(self, seed=12345):
        self.random_state = np.random.RandomState(seed)
        self.scores = [np.nan] * (self.GAME_NUMBER_FRAMES + 2)
        self.pins = [np.nan] * (self.GAME_NUMBER_FRAMES + 2)
        self.frame_type = [np.nan] * (self.GAME_NUMBER_FRAMES + 2)
        self.final_score = 0

        # todo: refactor all to use Frame instead of self.pins and self.frame_type.
        # for now use this to record the result of the frame
        self.frames: List[Frame] = []

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

    # org. todo: remove
    # def calc_score(self, pins, frame_idx, frame_type):
    #     if frame_idx >= self.GAME_NUMBER_FRAMES:
    #         return 0
    #     if frame_type == FrameTypes.NormalFrame:
    #         return self.calc_normal_score(pins, frame_idx)
    #     elif frame_type == FrameTypes.Spare:
    #         return self.calc_spare_score(pins, frame_idx)
    #     else:
    #         return self.calc_strike_score(pins, frame_idx)

    @staticmethod
    def throw_ball(rand_pins_probability: float, verbose: bool = False):
        assert 0 <= rand_pins_probability <= 1.0, "random pins probability must be a probability, i.e., [0, 1]"
        number_of_hit_pins = int(round(rand_pins_probability*10, 0))
        if verbose:
            print(number_of_hit_pins)
        return number_of_hit_pins

    def calc_frame_type(self, number_of_hit_pins: int, number_of_throws: int, frame_idx: int):
        if frame_idx >= self.GAME_NUMBER_FRAMES:
            return FrameTypes.NormalFrame
        elif number_of_hit_pins < self.NUMBER_OF_PINS:
            return FrameTypes.NormalFrame
        elif number_of_throws == 2:
            return FrameTypes.Spare
        else:
            return FrameTypes.Strike

    # todo: fix to work with frames only
    def play_frame(self, frame_idx: int):
        frame = Frame()

        number_of_throws = 1
        pins = self.throw_ball(self.random_state.random_sample(1)[0])
        frame.round.append(pins)
        if pins < self.NUMBER_OF_PINS:
            pins = min([self.NUMBER_OF_PINS, pins + self.throw_ball(self.random_state.random_sample(1)[0])])
            number_of_throws += 1
            frame.round.append(pins)
        frame_type = self.calc_frame_type(pins, number_of_throws, frame_idx)

        frame.frame_type = frame_type
        self.frames.append(frame)  # fixme: make this a returned value instead
        return pins, number_of_throws, frame_type

    # todo: remove when done
    # ORG
    # def play_frame(self, frame_idx: int):
    #     number_of_throws = 1
    #     pins = self.throw_ball(self.random_state.random_sample(1)[0])
    #     frame.pins_round_list.append(pins)
    #     if pins < self.NUMBER_OF_PINS:
    #         pins = min([self.NUMBER_OF_PINS, pins + self.throw_ball(self.random_state.random_sample(1)[0])])
    #         number_of_throws += 1
    #
    #     return pins, number_of_throws, frame_type

    def continue_game_indicator(self, frame_idx, pre_final_frame_type):
        if frame_idx < self.GAME_NUMBER_FRAMES - 1:
            return True

        if pre_final_frame_type == FrameTypes.NormalFrame:
            return False
        elif (pre_final_frame_type == FrameTypes.Spare) & (frame_idx < self.GAME_NUMBER_FRAMES + 1):
            return True
        elif (pre_final_frame_type == FrameTypes.Strike) & (frame_idx < self.GAME_NUMBER_FRAMES + 2):
            return True
        else:
            return False

    # todo: fixme
    # def game_scorer(self, pins: list, frame_types: list):
    #     frame_scores = []
    #     for frame_idx in range(0, self.GAME_NUMBER_FRAMES + 2):
    #         if pins[frame_idx] is np.nan:
    #             continue
    #
    #         frame_scores.append(self.calc_score(pins, frame_idx, frame_types[frame_idx]))
    #     return frame_scores

    # def play_game(self):
    #     for frame_idx in range(0, self.GAME_NUMBER_FRAMES + 2):
    #         if not self.continue_game_indicator(frame_idx, self.frame_type[frame_idx]):
    #             continue
    #
    #         pins, number_of_throws, frame_type = self.play_frame(frame_idx)
    #         self.pins[frame_idx] = pins
    #         self.frame_type[frame_idx] = frame_type
    #
    #     self.scores = self.game_scorer(self.pins, self.frame_type)
    #     self.final_score = sum(self.scores)
    #     print(f"final score: {self.final_score}")






    # todo: allow for custom player_skills distributions (for the sake of the kata, create several skill 'presets'
    # Default skill level: chances of hitting any number of pins from 0 to 10 is uniform
    # this is of course unrealistic
    # self.player_skill = player_skill  # the skill is array that contains probability of player to hit number of pins. The nth<->n+1 elements convey the probability to hit n pins
    # if self.player_skill is None:
    #     self.player_skill = np.linspace(0, 1, self.NUMBER_OF_PINS + 1)

