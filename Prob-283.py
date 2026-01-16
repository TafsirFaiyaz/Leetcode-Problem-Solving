class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        pos = 0 

        for i in range(len(nums)):              
            if nums[i] != 0:                    # If the current element is non-zero
                nums[pos] = nums[i]             # Move it to the 'pos' index
                pos += 1
                                                # What happened in the first loop is that all non-zero elements are moved to the front of the array in their original order.
                                                # Now, we need to fill the rest of the array with zeros.
        for i in range(pos, len(nums)):
            nums[i] = 0
