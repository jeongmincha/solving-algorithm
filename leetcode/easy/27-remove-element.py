# Problem: https://leetcode.com/problems/remove-element/

import unittest
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for num in nums:
            if num != val:
                nums[index] = num
                index += 1
        
        return index


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testRemoveElement(self):
        test_cases = [
            {
                'nums': [3,2,2,3],
                'val': 3,
                'output': 2
            },
            {
                'nums': [0,1,2,2,3,0,4,2],
                'val': 2,
                'output': 5
            }
        ]
        for test_case in test_cases:
            nums = test_case['nums']
            val = test_case['val']
            expected = test_case['output']
            answer = self.solution.removeElement(nums, val)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
