class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            else:
                if nums[mid] < nums[end]:
                    if nums[mid] <= target <= nums[end]:
                        start = mid+1
                    else:
                        end = mid-1
                else:
                    if nums[end] >= target or target >= nums[mid]:
                        start = mid+1
                    else:
                        end = mid-1

        return -1


solution = Solution()
nums = [4,5,6,7,0,1,2]
target = 7
print(solution.search(nums,target))

