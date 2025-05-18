from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            k = tuple(sorted(Counter(s).items()))
            result[k].append(s)
        return list(result.values())



if __name__ == '__main__':
    cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]])
    ]
    solution = Solution()
    for case in cases:
        res = solution.groupAnagrams(case[0])
        print(case[1], res)
