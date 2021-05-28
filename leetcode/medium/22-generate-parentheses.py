# Problem: https://leetcode.com/problems/generate-parentheses/

import unittest
from typing import List

class Solution:
    def __init__(self):
        self.result = []

    def generateParenthesisUtil(self, left: int, right: int, s: str):
        if left == 0 and right == 0:
            self.result.append(s)
            return
        if left > 0:
            self.generateParenthesisUtil(left-1, right, s+'(')
        if right > left:
            self.generateParenthesisUtil(left, right-1, s+')')

    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.generateParenthesisUtil(n, n, '')
        return self.result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testGenerateParenthesis(self):
        test_cases = [
            {
                'n': 3,
                'output': ['((()))', '(()())', '(())()', '()(())', '()()()']
            },
            {
                'n': 1,
                'output': ['()']
            }
        ]
        for test_case in test_cases:
            n = test_case['n']
            expected = test_case['output']
            answer = self.solution.generateParenthesis(n)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
