import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        last_val = 0
        q = []
        node = root
        while node is not None:
            q.append(node)
            node = node.left

        while len(q) > 0:
            node = q.pop()
            last_val = node.val
            k -= 1

            if k == 0:
                break

            if node.right is not None:
                q.append(node.right)
        
        return last_val


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testKthSmallest(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.left = None
        root.left.right = TreeNode(2)
        k = 1
        actual = self.solution.kthSmallest(root, k)
        expected = 1
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()