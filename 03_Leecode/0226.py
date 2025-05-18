# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self._invert(root)

    def _invert(self, node):
        if node is None:
            return None
        self._invert(node.left)
        self._invert(node.right)

        tmp = node.left
        node.left = node.right
        node.right = tmp
        return node


def construct_tree(level_order) -> TreeNode:
    queue = deque()
    root = TreeNode(level_order[0])
    queue.append(root)
    i = 1
    while queue and i < len(level_order):
        node = queue.popleft()
        if i < len(level_order):
            node.left = TreeNode(level_order[i]) if level_order[i] is not None else None
            queue.append(node.left)
            i += 1
        if i < len(level_order):
            node.right = TreeNode(level_order[i]) if level_order[i] is not None else None
            queue.append(node.right)
            i += 1
    return root


def level_order(root: TreeNode):
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
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1])
    ]

    solution = Solution()
    for input, answer in cases:
        tree = construct_tree(input)
        output = solution.invertTree(tree)
        print(answer, level_order(output))
