def parenthesis_matching(string) -> bool:
    """
    判断一个包含括号的字符串是否全部括号配对
    :return: True / False
    """
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in string:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs.keys():
            if len(stack)>0 and stack[-1] == bracket_pairs[char]:  # 配对成功
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(parenthesis_matching('(()))'))
    print(parenthesis_matching('(())()'))
