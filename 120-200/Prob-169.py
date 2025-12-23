class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        n = len(nums)
        if n < 2:
            return nums[0]
        for i in nums:
            if i in d:
                d[i] += 1
                if d[i] > n // 2:
                    return i
            else:
                d[i] = 1
        