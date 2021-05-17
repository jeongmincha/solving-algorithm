# Problem: https://leetcode.com/problems/search-a-2d-matrix-ii/

import unittest


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        i = m - 1
        j = 0

        while i >= 0 and j <= n - 1:
            if target > matrix[i][j]:
                j += 1
            elif target < matrix[i][j]:
                i -= 1
            else:
                return True

        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.prepared_matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ]

    def testSearchMatrix(self):
        target = 5
        actual = self.solution.searchMatrix(self.prepared_matrix, target)
        expected = True
        self.assertEqual(actual, expected)

    def testSearchMatrix2(self):
        target = 20
        actual = self.solution.searchMatrix(self.prepared_matrix, target)
        expected = False
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()