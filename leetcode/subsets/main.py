import unittest
from typing import List


class Solution:
    def num_to_bitarray(self, num: int, maxlen: int):
        bitarray = [0] * maxlen

        idx = len(bitarray)-1
        while num != 0:
            bitarray[idx] = num % 2
            idx -= 1
            num = int(num / 2)
        
        return bitarray

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        N = len(nums)

        for i in range(2 ** N):
            bit_array = self.num_to_bitarray(i, N)
            current = []
            for idx in range(len(bit_array)):
                if bit_array[idx] == 1:
                    current.append(nums[idx])
            result.append(current)

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testSubsets(self):
        nums = [1,2,3]
        expected = [
            [3],
            [1],
            [2],
            [1,2,3],
            [1,3],
            [2,3],
            [1,2],
            []
        ]
        actual = self.solution.subsets(nums)
        self.assertTrue(sorted(actual) == sorted(expected))


if __name__ == "__main__":
    unittest.main()
