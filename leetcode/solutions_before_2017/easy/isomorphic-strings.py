# Problem: https://leetcode.com/problems/isomorphic-strings/

import unittest


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for idx in range(len(s)):
            if s[idx] not in s_to_t:
                s_to_t[s[idx]] = t[idx]
            elif s_to_t[s[idx]] != t[idx]:
                return False

            if t[idx] not in t_to_s:
                t_to_s[t[idx]] = s[idx]
            elif t_to_s[t[idx]] != s[idx]:
                return False

        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testIsIsomorphic1(self):
        s = "egg"
        t = "add"
        expected = True
        actual = self.solution.isIsomorphic(s, t)
        self.assertEqual(expected, actual)

    def testIsIsomorphic2(self):
        s = "ab"
        t = "aa"
        expected = False
        actual = self.solution.isIsomorphic(s, t)
        self.assertEqual(expected, actual)

    def testIsIsomorphic3(self):
        s = "paper"
        t = "title"
        expected = True
        actual = self.solution.isIsomorphic(s, t)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
