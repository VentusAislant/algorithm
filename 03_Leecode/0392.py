class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ('abc', 'ahbgdc', True),
        ("axc", "ahbgdc", False),
    ]
    for case in cases:
        result = solution.isSubsequence(case[0], case[1])
        print(result, case[2])
