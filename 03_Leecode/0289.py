from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                around_live_count = 0
                l, t = i - 1 if i - 1 >= 0 else 0, j - 1 if j - 1 >= 0 else 0
                r, b = i + 1 if i + 1 < len(board) else i, j + 1 if j + 1 < len(board[i]) else j
                for x in range(l, r + 1):
                    for y in range(t, b + 1):
                        if (x, y) != (i, j):
                            if board[x][y] == 1 or board[x][y] == -1:
                                around_live_count += 1
                if board[i][j] == 0 and around_live_count == 3:
                    board[i][j] = 2  # dead -> alive  直接修改会影响后续算法

                if board[i][j] == 1:
                    if around_live_count < 2 or around_live_count > 3:
                        board[i][j] = -1  # alive -> dead

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]], [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]),
        ([[1, 1], [1, 0]], [[1, 1], [1, 1]]),
        ([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]], [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]])
    ]
    for case in cases:
        solution.gameOfLife(case[0])
        print(case[0], case[1])
