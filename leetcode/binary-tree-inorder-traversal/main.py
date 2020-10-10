import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        path = []
        stack = []

        while len(stack) is not 0 or root is not None:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                path.append(root.val)
                root = root.right

        return path

    def postorderTraversal(self, root):
        path = []
        stack = []
        peekNode = None
        lastVisitedNode = None

        while len(stack) is not 0 or root is not None:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                peekNode = stack[-1]
                if peekNode.right is not None and lastVisitedNode is not peekNode.right:
                    root = peekNode.right
                else:
                    path.append(peekNode.val)
                    lastVisitedNode = stack.pop()

        return path


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testInorderTraversal(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        expected = [1,3,2]
        actual = self.solution.inorderTraversal(root)
        self.assertEqual(expected, actual)

    def testPostorderTraversal(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        expected = [3,2,1]
        actual = self.solution.postorderTraversal(root)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()