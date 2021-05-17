# Problem: https://leetcode.com/problems/is-graph-bipartite/

import unittest
from typing import List


class Solution:
    def __init__(self):
        self.N = 0
        self.visited = None
        self.color = None

    def isBipartiteSubgraph(self, graph: List[List[int]], v) -> bool:
        for u in graph[v]:
            if self.visited[u] is False:
                self.visited[u] = True
                self.color[u] = -self.color[v]
                if self.isBipartiteSubgraph(graph, u) is False:
                    return False
            elif self.color[u] == self.color[v]:
                return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.N = len(graph)
        self.visited = [False] * self.N
        self.color = [0] * self.N

        idx = 0
        for idx in range(self.N):
            if len(graph[idx]) is not 0 and self.visited[idx] is False:
                self.color[idx] = 1
                if self.isBipartiteSubgraph(graph, idx) is False:
                    return False
        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testIsBipartiteTrue(self):
        graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
        actual = self.solution.isBipartite(graph)
        expected = True
        self.assertEqual(actual, expected)

    def testIsBipartiteFalse(self):
        graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
        actual = self.solution.isBipartite(graph)
        expected = False
        self.assertEqual(actual, expected)

    def testIsBipartiteComplex(self):
        graph = [
            [2, 4],
            [2, 3, 4],
            [0, 1],
            [1],
            [0, 1],
            [7],
            [9],
            [5],
            [],
            [6],
            [12, 14],
            [],
            [10],
            [],
            [10],
            [19],
            [18],
            [],
            [16],
            [15],
            [23],
            [23],
            [],
            [20, 21],
            [],
            [],
            [27],
            [26],
            [],
            [],
            [34],
            [33, 34],
            [],
            [31],
            [30, 31],
            [38, 39],
            [37, 38, 39],
            [36],
            [35, 36],
            [35, 36],
            [43],
            [],
            [],
            [40],
            [],
            [49],
            [47, 48, 49],
            [46, 48, 49],
            [46, 47, 49],
            [45, 46, 47, 48],
        ]
        actual = self.solution.isBipartite(graph)
        expected = False
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()