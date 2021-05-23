# Problem: https://leetcode.com/problems/merge-intervals/

import unittest
import operator


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "<start: {}, end: {}>".format(self.start, self.end)

    def __repr__(self):
        return "<start: {}, end: {}>".format(self.start, self.end)

    @classmethod
    def isEqualList(cls, intervals, lst):
        equal = True
        for idx in range(len(intervals)):
            if intervals[idx].start != lst[idx][0] or intervals[idx].end != lst[idx][1]:
                equal = False

        return equal

    @classmethod
    def convert(cls, lst):
        intervals = []
        for e in lst:
            intervals.append(Interval(e[0], e[1]))
        return intervals


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        stack = []

        # Sort intervals by start - O(N x logN)
        import operator

        intervals = sorted(intervals, key=operator.attrgetter("start"))

        for interval in intervals:
            if len(stack) == 0 or stack[-1] < interval.start:
                stack.append(interval.start)
                stack.append(interval.end)
            else:
                last = stack.pop()
                stack.append(max(interval.end, last))

        mergedIntervals = []
        for idx in range(0, len(stack), 2):
            interval = Interval(stack.pop(0), stack.pop(0))
            mergedIntervals.append(interval)

        return mergedIntervals


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def _checkAnswer(self, intervals, expected):
        print("\nInput: {} \nOutput: {}".format(intervals, expected))
        intervals = Interval.convert(intervals)
        actual = self.solution.merge(intervals)
        self.assertTrue(Interval.isEqualList(actual, expected))

    def testMerge1(self):
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        self._checkAnswer(intervals, expected)

    def testMerge2(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self._checkAnswer(intervals, expected)

    def testMerge3(self):
        intervals = [[0, 5], [1, 4]]
        expected = [[0, 5]]
        self._checkAnswer(intervals, expected)

    def testMerge4(self):
        intervals = [[2, 7], [1, 4]]
        expected = [[1, 7]]
        self._checkAnswer(intervals, expected)


if __name__ == "__main__":
    unittest.main()
