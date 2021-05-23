# Problem: https://leetcode.com/problems/zigzag-conversion/

import unittest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = ''
        rows = [[] for _ in range(numRows)]

        is_going_down = True
        current_row = 0
        
        for char in s:
            rows[current_row].append(char)

            if is_going_down:
                if current_row < numRows-1:
                    current_row += 1
                else:
                    is_going_down = False
                    current_row -= 1
            else:
                if current_row > 0:
                    current_row -= 1
                else:
                    is_going_down = True
                    current_row += 1

        return ''.join([''.join(row) for row in rows])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testConvert(self):
        test_cases = [
            {
                "s": "PAYPALISHIRING",
                "numRows": 3,
                "output": "PAHNAPLSIIGYIR"
            },
            {
                "s": "PAYPALISHIRING",
                "numRows": 4,
                "output": "PINALSIGYAHRPI"
            },
            {
                "s": "A",
                "numRows": 1,
                "output": "A"
            }
        ]
        for test_case in test_cases:
            s = test_case["s"]
            numRows = test_case["numRows"]
            expected = test_case["output"]
            answer = self.solution.convert(s, numRows)

            self.assertEqual(answer, expected)


if __name__ == '__main__':
    unittest.main()