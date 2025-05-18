from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        for k, v in s_counter.items():
            if k not in t_counter:
                return False
            else:
                if v != t_counter[k]:
                    return False

        for k, v in t_counter.items():
            if k not in s_counter:
                return False
            else:
                if v != s_counter[k]:
                    return False
        return True


if __name__ == '__main__':
    cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ]
    solution = Solution()
    for case in cases:
        res = solution.isAnagram(case[0], case[1])
        print(case[2], res)
