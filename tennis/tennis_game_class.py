
class Tennis:
    MIN_VICTORY_SCORE = 4
    SIMPLE_GAME_SCORE_THRESHOLD = 3

    SIMPLE_PHASE_SCORING_TRANSLATOR = {
        0: 'Love',
        1: '15',
        2: '30',
        3: '40'
    }

    def __init__(self):
    DEUCE = 'Deuce'
    ADVANTAGE = 'Advantage'
        self.group_1_score = 0
        self.group_2_score = 0

    def is_victory(self, score_1: int, score_2: int):
        return (abs(score_1 - score_2) >= 2) and any([score >= self.MIN_VICTORY_SCORE for score in [score_1, score_2]])

    def is_simple_game_phase(self, score_1: int, score_2: int):
        if self.is_deuce(score_1, score_2):
            return False
        elif score_1 <= self.SIMPLE_GAME_SCORE_THRESHOLD and score_2 <= self.SIMPLE_GAME_SCORE_THRESHOLD:
            return True
        else:
            return False

    def is_deuce(self, score_1: int, score_2: int):
        if score_1 == self.SIMPLE_GAME_SCORE_THRESHOLD and score_2 == self.SIMPLE_GAME_SCORE_THRESHOLD:
            return True
        elif score_1 == score_2 and score_1 > self.SIMPLE_GAME_SCORE_THRESHOLD:
            return True
        else:
            return False

    def simple_phase_score_translator(self, score_1, score_2):
        return [self.SIMPLE_PHASE_SCORING_TRANSLATOR[score_1], self.SIMPLE_PHASE_SCORING_TRANSLATOR[score_2]]

    def advanced_phase_score_translator(self, score_1, score_2):
        if self.is_deuce(score_1, score_2):
            return [self.DEUCE]
        elif score_1 > score_2:
            return [self.ADVANTAGE, None]
        else:
            return [None, self.ADVANTAGE]



    # def play(self):
    #     while not self.is_victory(self.group_1_score, self.group_2_score):




