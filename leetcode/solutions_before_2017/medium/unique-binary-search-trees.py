# Problem: https://leetcode.com/problems/unique-binary-search-trees/

import unittest


class Solution(object):
    def __init__(self):
        self.memo = {}
        self.memo[0] = 1
        self.memo[1] = 1

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.memo:
            return self.memo[n]

        result = 0
        for i in range(n):
            result += self.numTrees(i) * self.numTrees((n - 1) - i)

        self.memo[n] = result
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testNumTrees(self):
        n = 3
        actual = self.solution.numTrees(n)
        expected = 5
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()