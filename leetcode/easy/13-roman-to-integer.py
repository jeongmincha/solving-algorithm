# Problem: https://leetcode.com/problems/roman-to-integer/

import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        num = 0
        idx = 0
        while idx < len(s)-1:
            curr_int = roman_to_int[s[idx]]
            next_int = roman_to_int[s[idx+1]]
            if curr_int < next_int:
                num += (next_int - curr_int)
                idx += 2
            else:
                num += curr_int
                idx += 1
        
        if idx == len(s):
            return num
        else:
            return num + roman_to_int[s[-1]]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testRomanToInt(self):
        test_cases = [
            {
                's': 'III',
                'output': 3
            },
            {
                's': 'IV',
                'output': 4
            },
            {
                's': 'IX',
                'output': 9
            },
            {
                's': 'LVIII',
                'output': 58
            },
            {
                's': 'MCMXCIV',
                'output': 1994
            }
        ]
        for test_case in test_cases:
            s = test_case['s']
            expected = test_case['output']
            answer = self.solution.romanToInt(s)

            self.assertEqual(expected, answer)



if __name__ == '__main__':
    unittest.main()
