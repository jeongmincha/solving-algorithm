import unittest

class Solution:
    def permute(self, nums):
        from copy import deepcopy
        if len(nums) == 1:
            return [nums]
        
        prev_result = self.permute(nums[:-1])
        last = nums[-1]

        result = []
        for prev in prev_result:
            for idx in range(len(prev)+1):
                temp = deepcopy(prev)
                temp.insert(len(prev)-idx, last)
                result.append(temp)
                
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def testPermute(self):
        integers = [1,2,3]
        expected = [
            [1,2,3],
            [1,3,2],
            [2,1,3],
            [2,3,1],
            [3,1,2],
            [3,2,1]
        ]
        actual = self.solution.permute(integers)
        self.assertEqual(sorted(expected), sorted(actual))



if __name__ == "__main__":
    unittest.main()
