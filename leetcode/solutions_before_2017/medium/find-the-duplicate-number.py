# Problem: https://leetcode.com/problems/find-the-duplicate-number/

import unittest
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        find = 0
        while find != slow:
            slow = nums[slow]
            find = nums[find]

        return find


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testFindDuplicate(self):
        nums = [1, 3, 4, 2, 2]
        actual = self.solution.findDuplicate(nums)
        expected = 2
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
