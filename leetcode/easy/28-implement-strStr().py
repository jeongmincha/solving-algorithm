# Problem: https://leetcode.com/problems/implement-strstr/

import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1

        found = -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                found = i
                for j in range(len(needle)):
                    if haystack[i + j] != needle[j]:
                        found = -1
                        break
                if found != -1:
                    break

        return found


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testStrStr(self):
        test_cases = [
            {
                'haystack': 'hello',
                'needle': 'll',
                'output': 2
            },
            {
                'haystack': 'aaaaa',
                'needle': 'bba',
                'output': -1
            },
            {
                'haystack': '',
                'needle': '',
                'output': 0
            },
            {
                'haystack': 'aaa',
                'needle': 'aaa',
                'output': 0
            },
            {
                'haystack': 'aa',
                'needle': 'aab',
                'output': -1
            },
            {
                'haystack': 'bbaa',
                'needle': 'aaa',
                'output': -1
            }
        ]
        for test_case in test_cases:
            haystack = test_case['haystack']
            needle = test_case['needle']
            expected = test_case['output']
            answer = self.solution.strStr(haystack, needle)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
