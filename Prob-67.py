class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]    # Basic idea is to convert binary strings to integers, add them, and convert back to binary string.