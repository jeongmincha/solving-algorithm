# Problem: https://leetcode.com/problems/longest-palindromic-substring/

import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        start, length = 0, 0

        for end in range(len(s)):
            if s[end-length: end+1] == s[end-length: end+1][::-1]:
                start, length = end-length, length+1
            elif end-length > 0 and s[end-length-1: end+1] == s[end-length-1: end+1][::-1]:
                start, length = end-length-1, length+2
        
        return s[start:start+length]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testLongestPalindrome(self):
        test_cases = [
            {
                "s": "babad",
                "expected": "bab"
            },
            {
                "s": "cbbd",
                "expected": "bb"
            },
            {
                "s": "a",
                "expected": "a"
            },
            {
                "s": "ac",
                "expected": "a"
            },
            {
                "s": "aaaa",
                "expected": "aaaa"
            }
        ]

        for test_case in test_cases:
            s = test_case["s"]
            expected = test_case["expected"]

            answer = self.solution.longestPalindrome(s)
            self.assertEqual(answer, expected)


if __name__ == '__main__':
    unittest.main()