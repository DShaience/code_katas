from typing import List
from enum import Enum
import numpy as np

class RoundTypes(Enum):
    Normal = 0
    Spare = 1
    Strike = 2


class Bowling:
    GAME_NUMBER_FRAMES = 10
    NUMBER_OF_PINS = 10

    def __init__(self, seed=12345):
        self.random_state = np.random.RandomState(seed)
        self.scores = [None] * (self.GAME_NUMBER_FRAMES + 2)
        self.pins = [None] * (self.GAME_NUMBER_FRAMES + 2)
        self.round_type = [None] * (self.GAME_NUMBER_FRAMES + 2)
        self.number_of_played_rounds = 0

        # todo: allow for custom player_skills distributions (for the sake of the kata, create several skill 'presets'
        # Default skill level: chances of hitting any number of pins from 0 to 10 is uniform
        # this is of course unrealistic
        # self.player_skill = player_skill  # the skill is array that contains probability of player to hit number of pins. The nth<->n+1 elements convey the probability to hit n pins
        # if self.player_skill is None:
        #     self.player_skill = np.linspace(0, 1, self.NUMBER_OF_PINS + 1)

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

    # def play_frame(self):
        

