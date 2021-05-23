# Problem: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

import unittest
import heapq
from typing import List


class Solution:
    def heapify(self, heap, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2
        largest = idx

        if left < len(heap) and heap[left] > heap[largest]:
            largest = left
        if right < len(heap) and heap[right] > heap[largest]:
            largest = right

        if largest != idx:
            heap[largest], heap[idx] = heap[idx], heap[largest]
            self.heapify(heap, largest)

    def build_heap(self, heap):
        p = (len(heap) // 2) - 1
        while p >= 0:
            self.heapify(heap, p)
            p -= 1

    def extract_heap(self, heap):
        top = heap[0]
        heap[0] = heap[-1]
        del heap[-1]
        self.heapify(heap, 0)
        return top

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # n = len(matrix)
        # heap = []

        # for row in range(n):
        #     for col in range(n):
        #         heap.append(matrix[row][col])

        # self.build_heap(heap)
        # result = 0
        # for _ in range(len(heap)+1 - k):
        #     result = self.extract_heap(heap)

        # return result
        heap = []
        n = len(matrix)
        for row in range(n):
            for col in range(n):
                heapq.heappush(heap, matrix[row][col])
        return heapq.nsmallest(k, heap)[-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testKthSmallest(self):
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        k = 8
        actual = self.solution.kthSmallest(matrix, k)
        expected = 13
        self.assertEqual(actual, expected)

    def testKthSmallest2(self):
        matrix = [[1, 2], [1, 3]]
        k = 2
        actual = self.solution.kthSmallest(matrix, k)
        expected = 1
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()