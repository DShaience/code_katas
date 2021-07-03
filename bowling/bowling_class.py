from typing import List
from enum import Enum
import numpy as np


class FrameTypes(Enum):
    NormalFrame = 0
    Spare = 1
    Strike = 2
    FinalFrame = 3


class Bowling:
    GAME_NUMBER_FRAMES = 10
    NUMBER_OF_PINS = 10

    def __init__(self, seed=12345):
        self.random_state = np.random.RandomState(seed)
        self.scores = [np.nan] * (self.GAME_NUMBER_FRAMES + 2)
        self.pins = [np.nan] * (self.GAME_NUMBER_FRAMES + 2)
        self.frame_type = [np.nan] * (self.GAME_NUMBER_FRAMES + 2)
        self.number_of_played_frames = 0  # each frame may have up to 2 throws ("frames")

    def is_final_frame(self, frame: int):
        return frame == self.GAME_NUMBER_FRAMES

    @staticmethod
    def calc_strike_score(previous_frames_pins: List[int]):
        if len(previous_frames_pins) == 0:
            return 0
        else:
            return sum(previous_frames_pins)

    def calc_spare_score(self, previous_frames_pins: List[int]):
        return self.calc_strike_score(previous_frames_pins)

    @staticmethod
    def throw_ball(rand_pins_probability: float, verbose: bool = False):
        assert 0 <= rand_pins_probability <= 1.0, "random pins probability must be a probability, i.e., [0, 1]"
        number_of_hit_pins = int(round(rand_pins_probability*10, 0))
        if verbose:
            print(number_of_hit_pins)
        return number_of_hit_pins

    def calc_frame_type(self, number_of_hit_pins: int, number_of_throws: int, frame_idx: int):
        if frame_idx >= self.GAME_NUMBER_FRAMES:
            return FrameTypes.FinalFrame
        elif number_of_hit_pins < self.NUMBER_OF_PINS:
            return FrameTypes.NormalFrame
        elif number_of_throws == 2:
            return FrameTypes.Spare
        else:
            return FrameTypes.Strike

    def play_frame(self, frame_idx: int):
        number_of_throws = 1
        pins = self.throw_ball(self.random_state.random_sample(1)[0])
        if pins < self.NUMBER_OF_PINS:
            pins = min([self.NUMBER_OF_PINS, pins + self.throw_ball(self.random_state.random_sample(1)[0])])
            number_of_throws += 1
        frame_type = self.calc_frame_type(pins, number_of_throws, frame_idx)

        return pins, number_of_throws, frame_type

    def play_game(self):
        is_last_frame = False
        frame_idx = 0
        while not is_last_frame:
            pins, number_of_throws, frame_type = self.play_frame(frame_idx)
            self.pins[frame_idx] = pins
            self.frame_type[frame_idx] = frame_type
            if frame_type == FrameTypes.NormalFrame:
                self.scores[frame_idx] = pins

            frame_idx += 1
            # if

        # self.scores = [None] * (self.GAME_NUMBER_FRAMES + 2)
        # self.pins = [None] * (self.GAME_NUMBER_FRAMES + 2)
        # self.frame_type = [None] * (self.GAME_NUMBER_FRAMES + 2)




    # todo: allow for custom player_skills distributions (for the sake of the kata, create several skill 'presets'
    # Default skill level: chances of hitting any number of pins from 0 to 10 is uniform
    # this is of course unrealistic
    # self.player_skill = player_skill  # the skill is array that contains probability of player to hit number of pins. The nth<->n+1 elements convey the probability to hit n pins
    # if self.player_skill is None:
    #     self.player_skill = np.linspace(0, 1, self.NUMBER_OF_PINS + 1)

