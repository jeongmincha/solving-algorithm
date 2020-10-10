import unittest
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max_product = 1
        current_min_product = 1
        max_product = -float('inf')

        for num in nums:
            if num == 0:
                current_max_product = 0
                current_min_product = 1
            else:
                if num > 0:
                    current_max_product = current_max_product * num
                    current_min_product = min(current_min_product * num, 1)
                else:
                    temp = current_max_product
                    current_max_product = current_min_product * num
                    current_min_product = temp * num

            max_product = max(max_product, current_max_product)
            if current_max_product <= 0:
                current_max_product = 1
                
        return max_product


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testMaxProduct(self):
        nums = [2,3,-2,4]
        actual = self.solution.maxProduct(nums)
        expected = 6
        self.assertEqual(actual, expected)
    
    def testMaxProduct2(self):
        nums = [-2,0,-1]
        actual = self.solution.maxProduct(nums)
        expected = 0
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
