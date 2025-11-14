# Remove Element prob-27

class Solution(object):

    def removeElement(self, nums, val):

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:           # By doing this we are ignoring the val and replacing with a element which is not val
                nums[k] = nums[i]
                k += 1                    # Only incrementing k if nums[i] != val

        return k
        
