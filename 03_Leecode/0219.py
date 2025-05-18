from typing import List
from collections import defaultdict


class Solution:
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     num2index = defaultdict(list)
    #     for i, num in enumerate(nums):
    #         num2index[num].append(i)
    #     for i in range(len(nums)):
    #         if nums[i] in num2index and len(num2index[nums[i]]) > 1:
    #             for idx in num2index[nums[i]]:
    #                 if idx != i and abs(i - idx) <= k:
    #                     return True
    #     return False
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 用哈希表记录最近一次出现的位置
        nearby_num2idx = {}
        for i in range(len(nums)):
            if nums[i] in nearby_num2idx and i - nearby_num2idx[nums[i]] <= k:
                return True
            nearby_num2idx[nums[i]] = i
        return False


if __name__ == '__main__':
    cases = [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
    ]
    solution = Solution()
    for case in cases:
        res = solution.containsNearbyDuplicate(case[0], case[1])
        print(res, case[2])
