from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        pass




if __name__ == '__main__':
    cases = [
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2)
    ]
    solution = Solution()
    for case in cases:
        res = solution.findMinArrowShots(case[0])
        print(res, case[1])
