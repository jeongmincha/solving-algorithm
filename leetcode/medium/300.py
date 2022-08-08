# https://leetcode.com/problems/longest-increasing-subsequence/

import unittest
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    memo[i] = max(memo[i], 1 + memo[j])
        
        return max(memo)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testLengthOfLIS(self):
        test_cases = [
            [
                [10,9,2,5,3,7,101,18],
                4,
            ],
            [
                [7,7,7,7,7,7,7],
                1
            ],
            [
                [0,1,0,3,2,3],
                4
            ]
        ]
        for test_case in test_cases:
            nums, expected = test_case
            answer = self.solution.lengthOfLIS(nums)
            self.assertEqual(answer, expected)



if __name__ == '__main__':
    unittest.main()