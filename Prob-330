#330. Patching Array

#Basically the question is you have to see that if we can form 1 to n with the given numbers in nums. If not then there is a missing number

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        miss = 1            # Assuming this is the smallest number that is missing in the nums. 
        result = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:     # If the condition is False then it means we can form a number between miss and nums[i]
                miss += nums[i]
                i += 1

            else:
                miss += miss
                result += 1

        return result
        
