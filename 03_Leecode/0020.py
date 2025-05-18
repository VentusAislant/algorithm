class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(', ']': '[', '}':'{'}
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:

                if stack and pair[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True)
    ]
    solution = Solution()
    for s, a in cases:
        my_answer = solution.isValid(s)
        print(my_answer, a)
