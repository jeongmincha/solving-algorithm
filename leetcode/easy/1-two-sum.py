# Problem: https://leetcode.com/problems/two-sum/

import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = [-1, -1]
        hash_set = {}
        for index, num in enumerate(nums):
            if num in hash_set:
                answer = [hash_set[num], index]
                break
            hash_set[target - num] = index

        return answer


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testTwoSum(self):
        test_cases = [
            {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
            {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
            {"nums": [3, 3], "target": 6, "expected": [0, 1]},
        ]

        for test_case in test_cases:
            nums = test_case["num"]
            target = test_case["target"]
            expected = test_case["expected"]
            answer = self.solution.twoSum(nums, target)
            self.assertEqual(expected, answer)


if __name__ == "__main__":
    unittest.main()
