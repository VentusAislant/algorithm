class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_lst = []
        for char in s:
            if char.isalnum():
                char_lst.append(char.lower())

        left, right = 0, len(char_lst)-1
        while left < right:
            if char_lst[left] == char_lst[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True)
    ]
    solution = Solution()
    for s, answer in cases:
        my_answer = solution.isPalindrome(s)
        print(my_answer, answer)

