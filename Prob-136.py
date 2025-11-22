class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            res ^= n        # "^" means XOR operation. XOR operation because a^a=0 and a^0=a. So all duplicate numbers will cancel out each other. 
        return res
    
    
"""
nums = [4,1,2,1,2]
res = 0


res = 0 ^ 4 = 4
res = 4 ^ 1 = 5
res = 5 ^ 2 = 7
res = 7 ^ 1 = 6
res = 6 ^ 2 = 4
"""
# hopefully this explanation helps!