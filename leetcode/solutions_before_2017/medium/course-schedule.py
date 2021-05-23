# Problem: https://leetcode.com/problems/course-schedule/

import unittest
from typing import List


class Solution:
    def __init__(self):
        self.graph = {}
        self.visited = []
        self.recursion = []
        
    def isCyclic(self, v):
        self.visited[v] = True
        self.recursion[v] = True

        if v in self.graph:
            for neighbor in self.graph[v]:
                if self.visited[neighbor] is False:
                    if self.isCyclic(neighbor) is True:
                        return True
                elif self.recursion[neighbor] is True:
                    return True
        
        self.recursion[v] = False
        return False
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        self.visited = [False] * numCourses
        self.recursion = [False] * numCourses
        
        for prerequisite in prerequisites:
            later, first = prerequisite
            if first not in self.graph:
                self.graph[first] = [later]
            else:
                self.graph[first].append(later)
        
        for v in range(numCourses):
            if self.visited[v] is False and self.isCyclic(v) is True:
                return False
        return True
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testCanFinisihTrue(self):
        numCourses = 2
        prerequisites = [[1,0]]
        expected = True
        actual = self.solution.canFinish(numCourses, prerequisites)
        self.assertEqual(actual, expected)
    
    def testCanFinisihFalse(self):
        numCourses = 2
        prerequisites = [[1,0], [0,1]]
        expected = False
        actual = self.solution.canFinish(numCourses, prerequisites)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()