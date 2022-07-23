# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

import unittest
from typing import List


class Solution:
    def findIndexToAdd(self, sorted_nums: List[int], n: int) -> int:
        if len(sorted_nums) == 0:
            return 0

        left, right = 0, len(sorted_nums)-1
        while left <= right:
            mid = (left + right) // 2
            if n > sorted_nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return max(left, right)

    def countSmaller(self, nums: List[int]) -> List[int]:
        nums.reverse()

        sorted_nums = []
        indices = []

        for num in nums:
            index = self.findIndexToAdd(sorted_nums, num)
            sorted_nums.insert(index, num)
            indices.append(index)

        return indices[::-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testCountSmaller(self):
        test_cases = [
            [[5,2,6,1],[2,1,1,0]],
            [[-1],[0]],
            [[-1,-1],[0,0]]
        ]

        for test_case in test_cases:
            nums, expected = test_case
            answer = self.solution.countSmaller(nums)
            self.assertEqual(answer, expected)


if __name__ == "__main__":
    unittest.main()