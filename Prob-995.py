#995. Minimum Number of K Consecutive Bit Flips

class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        flipped = 0
        res = 0
        isFlipped = [0] * n
        
        for i in range(n):
            if i >= k:
                flipped ^= isFlipped[i - k]

            if flipped == nums[i]:
                if i + k > n:
                    return -1
                    
                isFlipped[i] = 1
                flipped ^= 1
                res += 1
        
        return res
        

