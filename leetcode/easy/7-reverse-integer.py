# Problem: https://leetcode.com/problems/reverse-integer/

import unittest


class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        answer = 0
        if x < 0:
            is_negative = True
            x = -x

        while x != 0:
            current_digit = x % 10
            if not (answer == 0 and current_digit == 0):
                answer = answer * 10 + current_digit
            x //= 10
        
        if is_negative:
            answer = -answer
        
        if answer > 2**31 - 1 or answer < -2**31:
            return 0
        else:
            return answer


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testReverse(self):
        test_cases = [
            {
                'x': 123,
                'output': 321
            },
            {
                'x': -123,
                'output': -321
            },
            {
                'x': 120,
                'output': 21
            },
            {
                'x': 0,
                'output': 0
            },
            {
                'x': 1534236469,
                'output': 0
            }
        ]
        for test_case in test_cases:
            x = test_case['x']
            expected = test_case['output']
            answer = self.solution.reverse(x)

            self.assertEqual(answer, expected)


if __name__ == '__main__':
    unittest.main()
