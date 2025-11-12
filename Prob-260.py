# 260. Single Number III

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor2no = 0
        
        for num in nums:
            xor2no ^= num

        lowestBit = xor2no & -xor2no

        result = [0, 0]
        for num in nums:
            if (lowestBit & num) == 0:
                result[0] ^= num
            else:
                result[1] ^= num

        return result
