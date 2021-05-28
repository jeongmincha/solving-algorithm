# Problem: https://leetcode.com/problems/4sum/

import unittest
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        answer = []
        nums.sort()
        n = len(nums)

        for i in range(n-3):
            if nums[i] == nums[i-1] and i > 0:
                continue
            for j in range(i+1, n-2):
                if nums[j] == nums[j-1] and j > i+1:
                    continue
                k, l = j+1, n-1
                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s < target:
                        k += 1
                    elif s > target:
                        l -= 1
                    else:
                        answer.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k+1]: k += 1
                        while k < l and nums[l] == nums[l-1]: l -= 1
                        k += 1
                        l -= 1

        return answer


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testFourSum(self):
        test_cases = [
            {
                'nums': [1,0,-1,0,-2,2],
                'target': 0,
                'output': [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
            },
            {
                'nums': [2,2,2,2,2],
                'target': 8,
                'output': [[2,2,2,2]]
            }
        ]
        for test_case in test_cases:
            nums = test_case['nums']
            target = test_case['target']
            expected = test_case['output']
            answer = self.solution.fourSum(nums, target)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
