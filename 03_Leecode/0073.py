from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        to_delete_i = set()
        to_delete_j = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    to_delete_i.add(i)
                    to_delete_j.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in to_delete_i or j in to_delete_j:
                    matrix[i][j] = 0


if __name__ == '__main__':
    cases = [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
    ]
    solution = Solution()
    for case in cases:
        solution.setZeroes(case[0])
        print(case[0], case[1])
