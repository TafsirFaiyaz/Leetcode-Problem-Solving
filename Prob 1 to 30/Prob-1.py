# Two sum prob-1

# This problem is finding if two numbers in a list sums upto target

class Solution(object):

    def twoSum(self, nums, target):
        N = len(nums)
    
        for i in range(N):
            
            for j in range(i+1,N):
       
                if nums[j] + nums[i] == target:        # Checking if the sum of i'th element and j'th element is the desired target
                 
                    return [i,j] 

        return []


'''
# Another solution by me which is optimized to O(n) time complexity (Most efficient way)

        numToIndex = {}

        for i in range(len(nums)):
            x = target - nums[i]    # x is what we need to add with nums[i] to find the target
             
            if x in numToIndex:           

                return [numToIndex[x], i]         

            numToIndex[nums[i]] = i

        return []

'''

'''
# Another Approach

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in nums:
                index = nums.index(compliment)  # Searching for the index number which holds the compliment value

                if index != i:    # Checking if the i'th value and index value is the same 
                    return index,i
        
        return []
'''

