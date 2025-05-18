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

if __name__ == '__main__':
    cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
    ]
    solution = Solution()
    for case in cases:
        res = solution.merge(case[0])
        print(res, case[1])
