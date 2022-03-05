"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000

"""
from typing import List


def rotate(matrix: List[List[int or str]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    if n == 1:
        return

    for p in range(0, n // 2):
        idx2 = n - p - 1
        for i in range(p, n-p-1):
            idx3 = n - 1 - i
            matrix[p][i], matrix[i][idx2], matrix[idx2][idx3], matrix[idx3][p] = matrix[idx3][p], matrix[p][i], matrix[i][idx2], matrix[idx2][idx3]


if __name__ == '__main__':
    matrix = [[2,29,20,26,16,28],
              [12,27,9,25,13,21],
              [32,33,32,2,28,14],
              [13,14,32,27,22,26],
              [33,1,20,7,21,7],
              [4,24,1,6,32,34]]
    n = len(matrix)

    expected = [[4, 33, 13, 32, 12, 2],
                [24, 1, 14, 33, 27, 29],
                [1, 20, 32, 32, 9,  20],
                [6,  7, 27, 2,  25, 26],
                [32, 21,22, 28, 13, 16],
                [34, 7, 26, 14, 21, 28]]

    true_false_matrix = []
    rotate(matrix)
    for i in range(n):
        true_false_matrix.append([matrix[i][j] == expected[i][j] for j in range(0, len(matrix[i]))])
        print(matrix[i])

    print("")
    for i in range(n):
        print(true_false_matrix[i])

    import numpy as np
    print(np.sum(np.array(true_false_matrix)))



# [1, 1] --> [1, 3]     [i, j] --> [[i, j+n-1]
# [1, 2] --> [2, 3]     [i+1, j] --> [[i+1, j+n-1]
# [1, 3] --> [3, 3]     [i+2, j] --> [[i+1, j+n-1]

# [1, 3] --> [3, 3]
# [2, 3] --> [3, 2]
# [3, 3] --> [3, 1]

# [3, 1] --> [1, 1]
# [2, 1] --> [1, 2]
# [1, 1] --> [1, 3]  # skip this swap, already did it.

# corners are [1, 1], [1, n], [n, n], [n, 1]
# on 0-based array
# corners are [0, 0], [0, n-1], [n-1, n-1], [n-1, 0]

# generalized:
# p=0
# corners are [0, 0], [0, 3],     [3, 3],         [3, 0]
#             [p, p], [p, n-p-1], [n-p-1, n-p-1], [n-p-1, p]

# p=1
# inner corners are  [1, 1], [1, 2],     [2, 2],         [2, 1]
#                    [p, p], [p, n-p-1], [n-p-1, n-p-1], [n-p-1, p]

# ['1','2','3','4',]
# ['5','6','7','8',]
# ['9','A','B','C',]
# ['D','E','F','10',]
