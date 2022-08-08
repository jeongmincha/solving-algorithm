# https://leetcode.com/problems/permutation-in-string/

import unittest

class Solution:
    def checkSame(self, counter1, counter2):
        same = True
        for c in counter1:
            if c not in counter2:
                same = False
            elif c in counter2 and counter1[c] != counter2[c]:
                same = False
        return same
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counter1 = {}
        counter2 = {} # counter hash map for sliding window of size len(s1)
        
        for c in set(s1):
            counter1[c] = 0
        for c in s1:
            counter1[c] += 1

        for c in set(s2):
            counter2[c] = 0
        for c in s2[:len(s1)]: # because it is for sliding window
            counter2[c] += 1

        if self.checkSame(counter1, counter2):
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            counter2[s2[l]] -= 1 # remove the passed one
            counter2[s2[r]] += 1 # add the new one
            l += 1
            
            if self.checkSame(counter1, counter2):
                return True

        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testCheckInclusion(self):
        test_cases = [
            [
                'a',
                'ab',
                True
            ],
            [
                'ab',
                'eidbaooo',
                True
            ],
            [
                'ab',
                'eidboaoo',
                False
            ],
            [
                'adc',
                'dcda',
                True
            ]
        ]
        for test_case in test_cases:
            [s1, s2, expected] = test_case
            answer = self.solution.checkInclusion(s1, s2)
            self.assertEqual(answer, expected)



if __name__ == "__main__":
    unittest.main()