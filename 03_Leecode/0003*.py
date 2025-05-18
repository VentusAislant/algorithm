class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            # 说明有重复的，左边界向右收缩
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            # 向右扩展
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len


if __name__ == '__main__':
    cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ]

    solution = Solution()
    for input, answer in cases:
        result = solution.lengthOfLongestSubstring(input)
        print(answer, result)
