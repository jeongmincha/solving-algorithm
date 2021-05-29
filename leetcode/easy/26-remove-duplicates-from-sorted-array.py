# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        
        answer = 1
        index = 0
        for num in nums[1:]:
            if num != nums[index]:
                index += 1
                nums[index] = num
                answer += 1
        
        while len(nums) > answer:
            del nums[-1]

        return answer


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testRemoveDuplicates(self):
        test_cases = [
            {
                'nums': [1,1,2],
                'output': 2
            },
            {
                'nums': [0,0,1,1,1,2,2,3,3,4],
                'output': 5
            }
        ]
        for test_case in test_cases:
            nums = test_case['nums']
            expected = test_case['output']
            answer = self.solution.removeDuplicates(nums)
            
            self.assertEqual(expected, answer)
            self.assertEqual(len(nums), expected)


if __name__ == '__main__':
    unittest.main()

