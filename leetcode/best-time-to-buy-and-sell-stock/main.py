import unittest


class Solution:
    def maxProfit(self, prices):
        max_so_far = 0
        max_ending_here = 0

        for idx in range(1, len(prices)):
            max_ending_here += prices[idx]-prices[idx-1]
            if max_ending_here < 0:
                max_ending_here = 0
            elif max_so_far < max_ending_here:
                max_so_far = max_ending_here

        return max_so_far


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testMaxProfit(self):
        prices = [7,1,5,3,6,4]
        expected = 5
        actual = self.solution.maxProfit(prices)
        self.assertEqual(actual, expected)

    def testMaxProfitNoCase(self):
        prices = [7,6,4,3,1]
        expected = 0
        actual = self.solution.maxProfit(prices)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()