from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        for k, v in ransomNote_count.items():
            if k not in magazine_count:
                return False
            else:
                if ransomNote_count[k] > magazine_count[k]:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ('a', 'b', False),
        ('aa', 'ab', False),
        ('aa', 'aab', True),
    ]
    for case in cases:
        res = solution.canConstruct(case[0], case[1])
        print(case[2], res)
