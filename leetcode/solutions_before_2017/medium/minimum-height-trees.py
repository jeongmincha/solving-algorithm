# Problem: https://leetcode.com/problems/minimum-height-trees/

import unittest
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return edges[0]

        adj = dict([(i, []) for i in range(n)])
        degree = [0 for _ in range(n)]

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
            degree[v1] += 1
            degree[v2] += 1

        q = []
        for i in range(n):
            if degree[i] is 1:
                q.append(i)

        while n > 2:
            qzise = len(q)
            for _ in range(qzise):
                t = q.pop(0)
                n -= 1

                for v in adj[t]:
                    degree[v] -= 1
                    if degree[v] is 1:
                        q.append(v)

        res = []
        while len(q) > 0:
            res.append(q.pop(0))

        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testFindMinHeightTrees(self):
        n = 4
        edges = [[1, 0], [1, 2], [1, 3]]
        actual = self.solution.findMinHeightTrees(n, edges)
        expected = [1]
        self.assertEqual(actual, expected)

    def testFindMinHeightTrees2(self):
        n = 6
        edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
        actual = self.solution.findMinHeightTrees(n, edges)
        expected = [3, 4]
        self.assertEqual(actual, expected)

    def testFindMinHeightTrees3(self):
        n = 9
        edges = [[0, 1], [0, 2], [2, 3], [0, 4], [2, 5], [5, 6], [3, 7], [0, 8]]
        actual = self.solution.findMinHeightTrees(n, edges)
        expected = [2]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()