# Problem: https://leetcode.com/problems/3sum/

import unittest
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        answer = []
        nums.sort()

        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            left, right = idx+1, len(nums)-1

            while left < right:
                sum3 = nums[idx] + nums[left] + nums[right]
                if sum3 < 0:
                    left += 1
                elif sum3 > 0:
                    right -= 1
                else:
                    answer.append([nums[idx], nums[left], nums[right]])
                    while left < len(nums)-1 and nums[left] == nums[left+1]:
                        left += 1
                    while right > 1 and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return answer


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testThreeSum(self):
        test_cases = [
            {
                'nums': [-1,0,1,2,-1,4],
                'output': [[-1,-1,2], [-1,0,1]]
            },
            {
                'nums': [],
                'output': []
            },
            {
                'nums': [0],
                'output': []
            },
            {
                'nums': [0,0,0,0],
                'output': [[0,0,0]]
            },
            {
                'nums': [-2,0,1,1,2],
                'output': [[-2,0,2], [-2,1,1]]
            }
        ]
        for test_case in test_cases:
            nums = test_case['nums']
            expected = test_case['output']
            answer = self.solution.threeSum(nums)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
