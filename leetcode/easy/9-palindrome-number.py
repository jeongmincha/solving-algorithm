# Problem: https://leetcode.com/problems/palindrome-number/

import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math

        if x < 0:
            return False
        
        copied_x = x
        reversed_x = 0

        while x != 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        
        return reversed_x == copied_x


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testIsPalindrome(self):
        test_cases = [
            {
                'x': 121,
                'output': True
            },
            {
                'x': -121,
                'output': False
            },
            {
                'x': 10,
                'output': False
            },
            {
                'x': -101,
                'output': False
            }
        ]
        for test_case in test_cases:
            x = test_case['x']
            expected = test_case['output']
            answer = self.solution.isPalindrome(x)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
