class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}    # num -> last index

        for i, num in enumerate(nums):               # i is the current index and num is the current number in nums
            if num in seen and i - seen[num] <= k:   # check if we have seen num before and if the distance is within k
                return True
            seen[num] = i                     # update the last index of num to the current index i                 

        return False
                
        