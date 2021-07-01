
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
        return score_1 == self.SIMPLE_GAME_SCORE_THRESHOLD and score_2 == self.SIMPLE_GAME_SCORE_THRESHOLD




