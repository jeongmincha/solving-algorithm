# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/

import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0

        n = len(nums)
        offset = 0
        left, right = 0, n-1
        while left < right:
            offset = (left + right) // 2
            if left == offset:
                break
            if nums[offset] > nums[right]:
                left = offset
            else:
                right = offset
        
        if right != 0:
            nums = nums[offset+1:] + nums[:offset+1]
        else:
            offset = -1

        answer = -1
        left, right = 0, n-1
        while left < right:
            mid = (left + right) // 2
            if target == nums[left]:
                answer = (left + offset + 1) % n
            elif target == nums[right]:
                answer = (right + offset + 1) % n
            elif target == nums[mid]:
                answer = (mid + offset + 1) % n

            if answer != -1:
                break
            elif left == mid:
                break

            if target > nums[mid]:
                left = mid
            elif target < nums[mid]:
                right = mid

        return answer


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testSearch(self):
        test_cases = [
            {
                'nums': [4,5,6,7,0,1,2],
                'target': 0,
                'output': 4
            },
            {
                'nums': [4,5,6,7,0,1,2],
                'target': 3,
                'output': -1
            },
            {
                'nums': [1],
                'target': 0,
                'output': -1
            },
            {
                'nums': [1],
                'target': 1,
                'output': 0
            },
            {
                'nums': [1,3],
                'target': 3,
                'output': 1
            },
            {
                'nums': [2,3,4,5,6,7,8,9,1],
                'target': 9,
                'output': 7
            }
        ]
        for test_case in test_cases:
            nums = test_case['nums']
            target = test_case['target']
            expected = test_case['output']
            answer = self.solution.search(nums, target)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
