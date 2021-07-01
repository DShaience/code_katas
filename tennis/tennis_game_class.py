
class Tennis:
    MIN_VICTORY_SCORE = 4

    def __init__(self):
        self.group_1_score = 0
        self.group_2_score = 0

    def is_victory(self, score_1: int, score_2: int):
        return (abs(score_1 - score_2) >= 2) and any([score >= self.MIN_VICTORY_SCORE for score in [score_1, score_2]])





