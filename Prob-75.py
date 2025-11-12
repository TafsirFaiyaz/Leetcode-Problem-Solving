#75. Sort Colors

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = 0
        n = len(nums)

        for i in range(2):
            for j in range(k,n):

                if nums[j] == i:
                    nums[k], nums[j] = nums[j], nums[k]
                    k += 1
        
