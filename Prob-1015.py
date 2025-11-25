class Solution(object):
    def smallestRepunitDivByK(self, k):
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        rem = 0
        
        for length in range(1, k + 1):
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return length
        
        return -1
    
    
# The question is asking for the smallest length of a number consisting of only 1's that is divisible by k.
# So just increase the number of 1's one by one and keep track of the remainder when divided by k.
# If at any point the remainder is 0, return the length of the number.