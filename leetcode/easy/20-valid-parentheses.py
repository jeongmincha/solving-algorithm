# Problem: https://leetcode.com/problems/valid-parentheses/

import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        matching = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = [s[0]]
        for c in s[1:]:
            if c in matching.keys():
                stack.append(c)
            elif len(stack) > 0 and stack[-1] in matching and matching[stack[-1]] == c:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testIsValid(self):
        test_cases = [
            {
                's': '()',
                'output': True
            },
            {
                's': '()[]{}',
                'output': True
            },
            {
                's': '(]',
                'output': False
            },
            {
                's': '([)]',
                'output': False
            },
            {
                's': '{[]}',
                'output': True
            }
        ]
        for test_case in test_cases:
            s = test_case['s']
            expected = test_case['output']
            answer = self.solution.isValid(s)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
