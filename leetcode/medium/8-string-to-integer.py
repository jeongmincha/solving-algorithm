# Problem: https://leetcode.com/problems/string-to-integer-atoi/

import unittest


class Solution:
    def myAtoi(self, s: str) -> int:
        answer = 0
        is_writing_integer = False
        is_negative = False
        char_to_digit = {str(k): k for k in range(10)}

        for char in s:
            if is_writing_integer:
                if char in char_to_digit.keys():
                    answer = answer * 10 + char_to_digit[char]
                else:
                    break
            else:
                if char in char_to_digit.keys():
                    status = 1
                    answer = char_to_digit[char]
                    is_writing_integer = True
                elif char == ' ':
                    continue
                elif char == '-':
                    is_negative = True
                    is_writing_integer = True
                elif char == '+':
                    is_writing_integer = True
                else:
                    answer = 0
                    break
        
        if is_negative:
            answer = -answer
        
        if answer < -2**31:
            return -2**31
        elif answer > 2**31-1:
            return 2**31-1
        else:
            return answer


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testMyAtoi(self):
        test_cases = [
            {
                's': '42',
                'output': 42
            },
            {
                's': '    -42',
                'output': -42
            },
            {
                's': '4193 with words',
                'output': 4193
            },
            {
                's': 'words and 987',
                'output': 0
            },
            {
                's': '-91283472332',
                'output': -2147483648
            }
        ]
        for test_case in test_cases:
            s = test_case['s']
            expected = test_case['output']
            answer = self.solution.myAtoi(s)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()