# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
import numpy as np

class RunnerScore:
    def __init__(self, score: int):
        self.score = score


if __name__ == '__main__':

    np.random.seed(90210)
    n = 10
    runner_scores = list(np.random.randint(-100, 100, n))
    print(runner_scores)

    max_score = runner_scores[0]
    prev_max = runner_scores[0]
    for i in range(1, len(runner_scores)):
        cur_score = runner_scores[i]
        if cur_score > max_score:
            prev_max = max_score
            max_score = cur_score
        elif cur_score > prev_max:
            prev_max = cur_score

    print(sorted(runner_scores)[::-1])
    print(prev_max)
    print(max_score)



