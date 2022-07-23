# https://leetcode.com/problems/two-sum/

import unittest
from typing import List


class Solution:
    # TC: O(N*logN)
    def _twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_index = [(num, idx) for idx, num in enumerate(nums)]
        nums_with_index.sort(key=lambda x:x[0])

        left, right = 0, len(nums)-1

        while left < right:
            sum_value = nums_with_index[left][0] + nums_with_index[right][0]
            if sum_value > target:
                right -= 1
            elif sum_value < target:
                left += 1
            else:
                break

        return [nums_with_index[left][1], nums_with_index[right][1]]
    
    # Better Solution
    # TC: O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(nums):
            if num in seen:
                if seen[num] > idx:
                    return [idx, seen[num]]
                else:
                    return [seen[num], idx]

            seen[target-num] = idx


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testTwoSum(self):
        test_cases = [
            [
                [2,7,11,15],
                9,
                [0,1]
            ],
            [
                [3,2,4],
                6,
                [1,2]
            ],
            [
                [3,3],
                6,
                [0,1]
            ]
        ]

        for test_case in test_cases:
            nums, target, expected = test_case
            answer = self.solution.twoSum(nums, target)
            self.assertEqual(answer, expected)


if __name__ == "__main__":
    unittest.main()
