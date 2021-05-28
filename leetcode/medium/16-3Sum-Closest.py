import unittest
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        answer = nums[0] + nums[1] + nums[2]
        for idx in range(n-2):
            left, right = idx+1, n-1
            while left < right:
                sum3 = nums[idx] + nums[left] + nums[right]
                answer = sum3 if abs(sum3 - target) < abs(answer - target) else answer
                if target == sum3:
                    return target
                elif target > sum3:
                    left += 1
                else:
                    right -= 1

        return answer


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testThreeSumClosest(self):
        test_cases = [
            {
                'nums': [-1, 2, 1, -4],
                'target': 1,
                'output': 2
            }
        ]
        for test_case in test_cases:
            nums = test_case['nums']
            target = test_case['target']
            expected = test_case['output']
            answer = self.solution.threeSumClosest(nums, target)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
