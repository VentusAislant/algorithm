from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.dfs(root, 0, targetSum)

    def dfs(self, node, cur_sum, target_sum):
        cur_sum += node.val
        if node.left is None and node.right is None:
            return cur_sum == target_sum

        left_res = False
        right_res = False
        if node.left:
            left_res = self.dfs(node.left, cur_sum, target_sum)
        if node.right:
            right_res = self.dfs(node.right, cur_sum, target_sum)
        return left_res or right_res


def construct_tree(level_order):
    if len(level_order) == 0:
        return None
    queue = deque()
    root = TreeNode(level_order[0])
    queue.append(root)
    i = 1
    while queue and i < len(level_order):
        node = queue.popleft()
        if i < len(level_order) and node:
            node.left = TreeNode(level_order[i]) if level_order[i] is not None else None
            queue.append(node.left)
            i += 1

        if i < len(level_order) and node:
            node.right = TreeNode(level_order[i]) if level_order[i] is not None else None
            queue.append(node.right)
            i += 1
    return root


def level_order(root: Optional[TreeNode]) -> List[int]:
    queue = deque()
    queue.append(root)
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


if __name__ == '__main__':
    cases = [
        (([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22), True),
        (([1, 2, 3], 5), False),
        (([], 0), False),
    ]
    solution = Solution()
    for input, answer in cases:
        output = solution.hasPathSum(construct_tree(input[0]), input[1])
        print(output, answer)
