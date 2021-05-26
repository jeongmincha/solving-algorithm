# Problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

import unittest
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        import copy
        digit_to_letter = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        answer = []
        for digit in digits:
            if len(answer) == 0:
                answer.extend(digit_to_letter[digit])
            else:
                original_answer = copy.copy(answer)
                for string in original_answer:
                    for letter in digit_to_letter[digit]:
                        answer.append(string + letter)
                answer = answer[len(original_answer):]

        return answer


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testLetterCombinations(self):
        test_cases = [
            {
                'digits': '23',
                'output': ["ad","ae","af","bd","be","bf","cd","ce","cf"]
            },
            {
                'digits': '',
                'output': []
            },
            {
                'digits': '2',
                'output': ["a","b","c"]
            }
        ]
        for test_case in test_cases:
            digits = test_case['digits']
            expected = test_case['output']
            answer = self.solution.letterCombinations(digits)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
