# Problem: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

import unittest


class Solution:
    # Time Complexity: O(N log N)
    # - worker들을 wage / quality 기준으로 sort하는데 O(N log N)
    # - worker들을 순회하면서 (N *) 힙에 추가하고(log N+), 힙에서 추출 (log N) -> O(N log N)
    # 따라서 전체 시간 복잡도 O(N log N)

    # Space Complexity: O(N)
    # - worker들을 따로 리스트에 저장했으므로 O(N)
    # - 힙의 크기를 K만큼 두었으므로 O(K)
    # 따라서 O(N+K) = O(N) (K < N 이므로)
    def mincostToHireWorkers(
        self, quality: "List[int]", wage: "List[int]", K: "int"
    ) -> "float":
        import heapq

        if K == 1:
            return min(wage)

        workers = [(w / q, q, w) for q, w in zip(quality, wage)]
        workers = sorted(workers, key=lambda x: x[0])

        min_cost = float("inf")
        sum_quality = 0
        heap = []
        for worker in workers:
            r, q, w = worker
            heapq.heappush(heap, q)
            heapq._heapify_max(heap)
            sum_quality += q

            if len(heap) > K:
                sum_quality -= heapq.heappop(heap)

            if len(heap) == K:
                min_cost = min(min_cost, sum_quality * r)

        return min_cost


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testMinCostToHireWorks1(self):
        quality = [10, 20, 5]
        wage = [70, 50, 30]
        K = 2
        actual = self.solution.mincostToHireWorkers(quality, wage, K)
        expected = 105
        self.assertLess(abs(actual - expected), 1e-5)

    def testMinCostToHireWorks2(self):
        quality = [3, 1, 10, 10, 1]
        wage = [4, 8, 2, 2, 7]
        K = 3
        actual = self.solution.mincostToHireWorkers(quality, wage, K)
        expected = 30.66667
        self.assertLess(abs(actual - expected), 1e-5)

    def testMinCostToHireWorks3(self):
        quality = [4, 5]
        wage = [8, 14]
        K = 2
        actual = self.solution.mincostToHireWorkers(quality, wage, K)
        expected = 25.2
        self.assertLess(abs(actual - expected), 1e-5)


if __name__ == "__main__":
    unittest.main()