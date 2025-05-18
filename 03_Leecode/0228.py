from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        if not nums: return []
        cur_start = nums[i]
        res = []
        while i < len(nums):
            if i < len(nums) - 1:
                if nums[i + 1] - nums[i] != 1:
                    if cur_start == nums[i]:
                        res.append(str(nums[i]))
                    else:
                        res.append(f"{cur_start}->{nums[i]}")
                    cur_start = nums[i + 1]
            else:
                if cur_start == nums[i]:
                    res.append(str(nums[i]))
                else:
                    res.append(f"{cur_start}->{nums[i]}")
            i += 1
        return res


if __name__ == '__main__':
    cases = [
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
    ]
    solution = Solution()
    for case in cases:
        res = solution.summaryRanges(case[0])
        print(res, case[1])
