from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for cur in intervals[1:]:
            last = res[-1]
            # 如何和前面的区间有重叠，则合并
            if cur[0] <= last[1]:
                last[1] = max(last[1], cur[1])
            else:
                res.append(cur)
        return res

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)


if __name__ == '__main__':
    cases = [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]])
    ]
    solution = Solution()
    for case in cases:
        res = solution.insert(case[0], case[1])
        print(res, case[2])
