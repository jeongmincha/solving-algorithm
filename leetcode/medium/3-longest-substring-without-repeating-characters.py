# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/

import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        start = 0
        found_index = {}

        for end, char in enumerate(s):
            if (char in found_index) and (start <= found_index[char]):
                start = found_index[char] + 1
            else:
                answer = max(answer, end + 1 - start)
            
            found_index[char] = end
        
        return answer



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testLengthOfLongestSubstring(self):
        test_cases = [
            {
                "s": "abcabcbb",
                "expected": 3
            },
            {
                "s": "bbbbb",
                "expected": 1
            },
            {
                "s": "pwwkew",
                "expected": 3
            },
            {
                "s": "",
                "expected": 0
            },
            {
                "s": "dvdf",
                "expected": 3
            }
        ]
        for test_case in test_cases:
            s = test_case['s']
            expected = test_case['expected']
            answer = self.solution.lengthOfLongestSubstring(s)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
