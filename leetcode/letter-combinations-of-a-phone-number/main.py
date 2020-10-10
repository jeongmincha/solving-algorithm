import unittest

class Solution:
    def __init__(self):
        self.answer = []
        self.charMap = {
          '2': 'abc',
          '3': 'def',
          '4': 'ghi',
          '5': 'jkl',
          '6': 'mno',
          '7': 'pqrs',
          '8': 'tuv',
          '9': 'wxyz',
        }

    def searchAnswer(self, digits, idx=0, output=""):
        if len(digits) == idx:
            self.answer.append(output)
            return

        if digits[idx] == 0 or digits[idx] == 1:
            return

        for c in self.charMap[digits[idx]]:
            self.searchAnswer(digits, idx+1, output + c)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        self.searchAnswer(digits)

        return self.answer


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testLetterCombinations(self):
        actual = self.solution.letterCombinations('23')
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

        self.assertEqual(sorted(actual), sorted(expected))


if __name__ == '__main__':
  unittest.main()
