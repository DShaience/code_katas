"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1

Follow up:
    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
"""

from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    cols_set = set()
    rows_set = set()
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):

            if matrix[row][col] == 0:
                rows_set.add(row)
                cols_set.add(col)

    for row in range(rows):
        for col in range(cols):
            if (row in rows_set) or (col in cols_set):
                matrix[row][col] = 0





if __name__ == '__main__':
    # matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    # expected = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    expected = [[0,0,0,0],[0,0,0,4],[0,0,0,0],[0,0,0,3],[0,0,0,0]]
    setZeroes(matrix)
    print(matrix)


