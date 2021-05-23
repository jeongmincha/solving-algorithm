# Problem: https://leetcode.com/problems/course-schedule-ii/

import unittest
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        indegrees = {}
        for node in range(numCourses):
            graph[node] = []
            indegrees[node] = 0

        for prerequisite in prerequisites:
            later, first = prerequisite
            graph[first].append(later)
            indegrees[later] += 1

        path = []
        for node in range(numCourses):
            existZeroDegreeNode = False
            for v in range(numCourses):
                if indegrees[v] == 0:
                    existZeroDegreeNode = True
                    break
            if not existZeroDegreeNode:
                return []

            # Add zero degree node to path and remove it from the graph
            indegrees[v] -= 1
            path.append(v)
            for neighbor in graph[v]:
                indegrees[neighbor] -= 1

        return path


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testFindOrder1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        expected = [0, 1]
        actual = self.solution.findOrder(numCourses, prerequisites)
        self.assertEqual(actual, expected)

    def testFindOrder2(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        expected = [[0, 1, 2, 3], [0, 2, 1, 3]]
        actual = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(actual == expected[0] or actual == expected[1])


if __name__ == "__main__":
    unittest.main()