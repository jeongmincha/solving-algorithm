# Problem: https://leetcode.com/problems/integer-to-roman/

import unittest


class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        answer = ''

        while num > 0:
            for value in int_to_roman.keys():
                if num >= value:
                    answer += int_to_roman[value]
                    num -= value
                    break

        return answer

    # def intToRoman(self, num: int) -> str:
    #     answer = ''
    #     while num > 0:
    #         if 0 < num // 1000 < 4:
    #             answer += 'M' * (num // 1000)
    #             num %= 1000
    #         elif num // 100 == 9:
    #             answer += 'CM'
    #             num -= 900
    #         elif 0 < num // 500:
    #             answer += 'D'
    #             num -= 500
    #         elif num // 100 == 4:
    #             answer += 'CD'
    #             num -= 400
    #         elif 0 < num // 100 < 4:
    #             answer += 'C' * (num // 100)
    #             num %= 100
    #         elif num // 10 == 9:
    #             answer += 'XC'
    #             num -= 90
    #         elif 0 < num // 50:
    #             answer += 'L'
    #             num -= 50
    #         elif num // 10 == 4:
    #             answer += 'XL'
    #             num -= 40
    #         elif 0 < num // 10 < 4:
    #             answer += 'X' * (num // 10)
    #             num %= 10
    #         elif num == 9:
    #             answer += 'IX'
    #             num -= 9
    #         elif 0 < num // 5:
    #             answer += 'V'
    #             num -= 5
    #         elif num == 4:
    #             answer += 'IV'
    #             break
    #         else:
    #             answer += 'I' * num
    #             break
        
    #     return answer


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testIntToRoman(self):
        test_cases = [
            # {
            #     'num': 3,
            #     'output': 'III'
            # },
            # {
            #     'num': 4,
            #     'output': 'IV'
            # },
            # {
            #     'num': 9,
            #     'output': 'IX'
            # },
            # {
            #     'num': 58,
            #     'output': 'LVIII'
            # },
            {
                'num': 1994,
                'output': 'MCMXCIV'
            }
        ]
        for test_case in test_cases:
            num = test_case['num']
            expected = test_case['output']
            answer = self.solution.intToRoman(num)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
