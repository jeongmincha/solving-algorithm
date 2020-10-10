import sys
import unittest
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1 = len(nums1)
        n2 = len(nums2)

        if k == 0 or n1 == 0 or n2 == 0:
            return []

        pairs = []
        index2 = [0 for i in range(n1)]
        
        while k > 0:
            min_sum = sys.maxsize
            min_idx = 0

            for idx1 in range(len(nums1)):
                idx2 = index2[idx1]
                if (idx2 < n2 and nums1[idx1] + nums2[idx2] < min_sum):
                    min_idx = idx1
                    min_sum = nums1[idx1] + nums2[index2[idx1]]

            if index2[min_idx] < n2:
                pairs.append([nums1[min_idx], nums2[index2[min_idx]]])
            index2[min_idx] += 1
            k -= 1

        return pairs

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testkSmallestPairs(self):
        nums1 = [1,7,11]
        nums2 = [2,4,6]
        k = 3
        actual = self.solution.kSmallestPairs(nums1, nums2, k)
        expected = [[1,2], [1,4], [1,6]]
        self.assertEqual(set(tuple(_) for _ in actual), set(tuple(_) for _ in expected))

    def testkSmallestPairs2(self):
        nums1 = [1,2]
        nums2 = [3]
        k = 3
        actual = self.solution.kSmallestPairs(nums1, nums2, k)
        expected = [[1,3],[2,3]]
        self.assertEqual(set(tuple(_) for _ in actual), set(tuple(_) for _ in expected))

    def testkSmallestPairs3(self):
        nums1 = [1,1,2]
        nums2 = [1,2,3]
        k = 10
        actual = self.solution.kSmallestPairs(nums1, nums2, k)
        expected = [[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]
        self.assertEqual(set(tuple(_) for _ in actual), set(tuple(_) for _ in expected))
    
    def testkSmallestPairs4(self):
        nums1 = [1,1,2]
        nums2 = [1,2,3]
        k = 2
        actual = self.solution.kSmallestPairs(nums1, nums2, k)
        expected = [[1,1],[1,1]]
        self.assertEqual(set(tuple(_) for _ in actual), set(tuple(_) for _ in expected))

if __name__ == "__main__":
    unittest.main()