# Problem: https://leetcode.com/problems/most-profit-assigning-work/

import unittest
from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        jobs = sorted([(a, b) for a, b in zip(difficulty, profit)])
        print(jobs)

        max_p = 0
        i = 0
        result = 0
        for w in sorted(worker):
            while i < len(jobs) and w >= jobs[i][0]:
                max_p = max(max_p, jobs[i][1])
                i += 1
            result += max_p
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testMaxProfitAssignment(self):
        difficulty = [2, 4, 6, 8, 10]
        profit = [10, 20, 30, 40, 50]
        worker = [4, 5, 6, 7]
        actual = self.solution.maxProfitAssignment(difficulty, profit, worker)
        expected = 100
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()