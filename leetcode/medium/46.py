# https://leetcode.com/problems/permutations/

import unittest
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def helper(current: List[int], remaining: List[int]):
            if len(remaining) == 0:
                answer.append(current)
                return
            
            for idx, char in enumerate(remaining):
                helper(current + [char], remaining[0:idx]+remaining[idx+1:])
        
        helper([], nums)
        return answer

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testPermute(self):
        test_cases = [
            [
                [1,2,3],
                [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
            ],
            [
                [0,1],
                [[1,0],[0,1]]
            ],
            [
                [1],
                [[1]]
            ]
        ];

        for test_case in test_cases:
            [nums, expected] = test_case
            answer = self.solution.permute(nums)
            self.assertCountEqual(answer, expected) # list equals

if __name__ == '__main__':
    unittest.main()