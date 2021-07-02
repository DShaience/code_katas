from typing import List


class Bowling:
    GAME_NUMBER_FRAMES = 10

    def __init__(self):
        self.scores = [None] * (self.GAME_NUMBER_FRAMES + 2)
        self.pins = [None] * (self.GAME_NUMBER_FRAMES + 2)
        self.round_type = [None] * (self.GAME_NUMBER_FRAMES + 2)

    def is_final_frame(self, frame: int):
        return frame == self.GAME_NUMBER_FRAMES

    @staticmethod
    def calc_strike_score(previous_frames_pins: List[int]):
        if len(previous_frames_pins) == 0:
            return 0
        else:
            return sum(previous_frames_pins)






