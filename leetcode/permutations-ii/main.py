import unittest

class Solution:
    def permuteUnique(self, nums):
        from copy import deepcopy
        if len(nums) == 1:
            return [nums]
        
        prev_result = self.permuteUnique(nums[:-1])
        last = nums[-1]

        result = []
        for prev in prev_result:
            for idx in range(len(prev)+1):
                temp = deepcopy(prev)
                temp.insert(len(prev)-idx, last)
                if temp not in result:
                    result.append(temp)

        return result

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testPermuteUnique(self):
        inputs = [1,1,2]
        expected = [
            [1,1,2],
            [1,2,1],
            [2,1,1]
        ]
        actual = self.solution.permuteUnique(inputs)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()