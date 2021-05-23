# Problem: https://leetcode.com/problems/container-with-most-water/

import unittest
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left, right = 0, len(height)-1

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            answer = max(answer, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return answer


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testMaxArea(self):
        test_cases = [
            # {
            #     'height': [1,1],
            #     'output': 1
            # },
            # {
            #     'height': [4,3,2,1,4],
            #     'output': 16
            # },
            # {
            #     'height': [1,2,1],
            #     'output': 2
            # },
            # {
            #     'height': [1,8,6,2,5,4,8,3,7],
            #     'output': 49
            # },
            {
                'height': [2,3,4,5,18,17,6],
                'output': 17
            }
        ]
        for test_case in test_cases:
            height = test_case['height']
            expected = test_case['output']
            answer = self.solution.maxArea(height)

            self.assertEqual(expected, answer)


if __name__ == '__main__':
    unittest.main()
