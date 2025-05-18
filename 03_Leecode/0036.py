from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != '.':
                    box_id = row // 3 * 3 + col // 3
                    if board[row][col] in row_sets[row] or \
                            board[row][col] in col_sets[col] or \
                            board[row][col] in box_sets[box_id]:
                        return False
                    else:
                        row_sets[row].add(board[row][col])
                        col_sets[col].add(board[row][col])
                        box_sets[box_id].add(board[row][col])
        return True


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (
            [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
            True
        ),
        (
            [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
            False
        )
    ]

    for case in cases:
        result = solution.isValidSudoku(case[0])
        print(result, case[1])
