# Easy Approach
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
        
        
# Better Approach

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)                       # Sum of elements in the array
        r = sum(range(len(nums)+1))         # Sum of first n natural numbers
        return r - s             # The missing number is the difference between the two sums
        