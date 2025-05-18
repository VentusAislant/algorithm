from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        cur_sum = 0
        min_len = float('inf')
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                # 收缩左边界
                cur_sum -= nums[left]
                left += 1

        if min_len == float('inf'):
            return 0
        else:
            return min_len


if __name__ == '__main__':
    solution = Solution()
    cases = [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0)
    ]
    for case in cases:
        result = solution.minSubArrayLen(case[0], case[1])
        print(result, case[2])
