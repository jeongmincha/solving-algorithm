# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/

import unittest
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        stack = [[root]]

        result = []
        while len(stack) > 0:
            nodes = stack.pop()

            current_result = []
            for node in nodes:
                if node is not None:
                    current_result.append(node.val)
            if len(current_result) > 0:
                result.append(current_result)

            next = []
            for node in nodes:
                if node is None:
                    continue
                if node.left is not None:
                    next.append(node.left)
                if node.right is not None:
                    next.append(node.right)

            if len(next) > 0:
                stack.append(next)

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testLevelOrder(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        actual = self.solution.levelOrder(root)
        expected = [[3], [9, 20], [15, 7]]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()