from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seen = set()
        max_len = 0
        for num in nums:
            if num in seen:
                continue
            cur_num = num
            cur_len = 1
            seen.add(cur_num)
            while cur_num + 1 in nums:
                seen.add(cur_num+1)
                cur_num += 1
                cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len



if __name__ == '__main__':
    cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
    ]
    solution = Solution()
    for case in cases:
        res = solution.longestConsecutive(case[0])
        print(res, case[1])
