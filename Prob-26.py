#26. Remove Duplicates from Sorted Array

# As the nums is sorted the duplicate value will be in consecutive positions

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
                                    
        k=1                               # k is the output  
        for i in range(1,len(nums)):        

            if nums[i] != nums[i-1]:      # If there exist a duplicate value it will ignore and k won't increment. If again we find a unique value then it will be swap to k'th position
                nums[k] = nums[i]              
                k += 1 

        return k
