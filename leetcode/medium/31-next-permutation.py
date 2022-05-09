# Problem: https://leetcode.com/problems/next-permutation/

import unittest
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = -1, -1

        # find i: last index which nums[idx] < nums[idx+1]
        for idx in range(n-2, -1, -1):
            if nums[idx] < nums[idx+1]:
                i = idx
                break

        if i > -1:
            # find j: last index which > nums[i]
            for idx in range(n-1, 0, -1):
                if nums[idx] > nums[i]:
                    j = idx
                    break

            # swap nums[i] & nums[j]
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        # reverse orders after i
        for idx in range(i+1, (n+i+1) // 2):
            temp = nums[idx]
            nums[idx] = nums[n - (idx - i)]
            nums[n - (idx - i)] = temp


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testNextPermutation(self):
        test_cases = [
            {
                'nums': [1,2,3],
                'output': [1,3,2]
            },
            {
                'nums': [3,2,1],
                'output': [1,2,3]
            },
            {
                'nums': [1,1,5],
                'output': [1,5,1]
            },
            {
                'nums': [1,3,2],
                'output': [2,1,3]
            }
        ]
        for test_case in test_cases:
            nums = test_case['nums']
            expected = test_case['output']
            self.solution.nextPermutation(nums)

            self.assertEqual(nums, expected)


if __name__ == '__main__':
    unittest.main()
