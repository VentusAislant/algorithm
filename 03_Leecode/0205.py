class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st = {}
        map_ts = {}
        for ch_s, ch_t in zip(s, t):
            if (ch_s in map_st and map_st[ch_s] != ch_t) or \
                    (ch_t in map_ts and map_ts[ch_t] != ch_s):
                return False
            map_st[ch_s] = ch_t
            map_ts[ch_t] = ch_s
        return True


if __name__ == '__main__':
    solution = Solution()
    cases = [
        ('egg', 'add', True),
        ('foo', 'bar', False),
        ('paper', 'title', True),
    ]
    for case in cases:
        res = solution.isIsomorphic(case[0], case[1])
        print(case[2], res)
