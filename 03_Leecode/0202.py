class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            new_n = 0
            cur_pos = n
            while cur_pos > 0:
                new_n += (cur_pos % 10) ** 2
                cur_pos //= 10
            n = new_n

        return True


if __name__ == '__main__':
    cases = [
        (19, True),
        (2, False),
    ]
    solution = Solution()
    for case in cases:
        res = solution.isHappy(case[0])
        print(res, case[1])
