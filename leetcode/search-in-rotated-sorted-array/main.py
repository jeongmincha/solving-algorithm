import unittest


class Solution:
    def __init__(self):
        self.start_idx = -1

    def find_start(self, nums, start, end):
        mid = (start + end) // 2

        if start < end:
            if nums[mid] > nums[mid+1]:
                self.start_idx = mid+1
            else:
                self.find_start(nums, start, mid-1)
                self.find_start(nums, mid+1, end)
        elif self.start_idx == -1:
            self.start_idx = 0

    def find(self, nums, start, end, target):
        mid = (start + end) // 2

        if start <= end:
            if nums[mid] == target:
                return mid
            else:
                result1 = self.find(nums, start, mid-1, target)
                result2 = self.find(nums, mid+1, end, target)

                if result1 != -1:
                    return result1
                elif result2 != -1:
                    return result2
                else:
                    return -1
        else:
            return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        # Find the start point and make nums back as sorted -> O(log N)
        self.find_start(nums, 0, len(nums) - 1)
        if self.start_idx > 0:
            nums = nums[self.start_idx:] + nums[:self.start_idx]
        print(nums)

        # Find the target - O(log N)
        idx = self.find(nums, 0, len(nums)-1, target)
        if idx != -1:
            return (idx + self.start_idx) % len(nums)
        else:
            return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testSearch1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0

        actual = self.solution.search(nums, target)
        expected = 4
        self.assertEqual(actual, expected)

    def testSearch2(self):
        nums = [3, 1]
        target = 3

        actual = self.solution.search(nums, target)
        expected = 0
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()