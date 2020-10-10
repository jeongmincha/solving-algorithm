import unittest


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        path = []

        cur_row = 0
        cur_col = 0
        end_row = len(matrix)
        end_col = len(matrix[0])

        while cur_row < end_row and cur_col < end_col:
            # Trace the current row
            for col in range(cur_col, end_col):
                path.append(matrix[cur_row][col])
            cur_row += 1

            # Trace the last column
            for row in range(cur_row, end_row):
                path.append(matrix[row][end_col-1])
            end_col -= 1

            # Trace the last row
            if cur_row < end_row:
                for col in range(end_col-1, cur_col-1, -1):
                    path.append(matrix[end_row-1][col])
                end_row -= 1
            
            # Trace the first column
            if cur_col < end_col:
                for row in range(end_row-1, cur_row-1, -1):
                    path.append(matrix[row][cur_col])
                cur_col += 1

        return path
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testSpiralOrder1(self):
        matrix = [
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ]
        expected = [1,2,3,6,9,8,7,4,5]

        actual = self.solution.spiralOrder(matrix)
        self.assertEqual(actual, expected)

    def testSpiralOrder2(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9,10,11,12]
        ]
        expected = [1,2,3,4,8,12,11,10,9,5,6,7]

        actual = self.solution.spiralOrder(matrix)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
