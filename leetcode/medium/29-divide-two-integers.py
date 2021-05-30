# Problem: https://leetcode.com/problems/divide-two-integers/

import unittest


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = dividend // divisor
        if dividend % divisor != 0 and dividend * divisor < 0:
            result += 1

        if result > 2**31-1 or result < -2**31:
            return 2**31-1
        else:
            return result


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testDivide(self):
        test_cases = [
            {
                'dividend': 10,
                'divisor': 3,
                'output': 3
            },
            {
                'dividend': 7,
                'divisor': -3,
                'output': -2
            },
            {
                'dividend': 0,
                'divisor': 1,
                'output': 0
            },
            {
                'dividend': 1,
                'divisor': 1,
                'output': 1
            },
            {
                'dividend': -1,
                'divisor': 1,
                'output': -1
            }
        ]
        for test_case in test_cases:
            dividend = test_case['dividend']
            divisor = test_case['divisor']
            expected = test_case['output']
            answer = self.solution.divide(dividend, divisor)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
