import unittest


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left = [1]
        right = [1]

        for num in nums[:-1]:
            left.append(left[-1] * num)
        
        for num in reversed(nums[1:]):
            right.insert(0, right[0] * num)

        prod = []
        for idx in range(n):
            prod.append(left[idx] * right[idx])

        return prod

    def productExceptSelfSmallSpace(self, nums):
        n = len(nums)
        prod = []
        temp = 1

        for num in nums:
            prod.append(temp)
            temp = prod[-1] * num
        
        temp = 1
        for idx in range(n-1, -1, -1):
            prod[idx] *= temp
            temp *= nums[idx]
        
        return prod


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testProductExceptSelf(self):
        nums = [2, 3, 4, 5]
        expected = [60, 40, 30, 24]
        actual = self.solution.productExceptSelf(nums)
        self.assertEqual(expected, actual)
        
        actual = self.solution.productExceptSelfSmallSpace(nums)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
