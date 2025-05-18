from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l + 1, r + 1]
            elif curr_sum < target:
                l += 1
            else:
                r -= 1
        return []

if __name__ == '__main__':
    solution = Solution()
    cases = [
        ([3, 24, 50, 79, 88, 150, 345], 200, [3, 6]),
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([0, 0, 3, 4], 0, [1, 2]),
        ([5, 25, 75], 100, [2, 3]),
        ([-5, -3, 0, 2, 4, 6, 8], 5, [2, 7]),
    ]
    for case in cases:
        result = solution.twoSum(case[0], case[1])
        print(case[0], case[1], result, case[2])
