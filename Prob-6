# 6. Zigzag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [[] for row in range(numRows)]
        index = 0
        step = -1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)
        
'''
# Another Solution

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>len(s):
            return s
            
        d = ['' for i in range(numRows)]
        curr = 0
        mode = 0

        for c in s:

            d[curr]+=c
            if curr==0:
                mode = 1
            elif curr==numRows-1:
                mode = -1
            curr = curr + mode

        return "".join(d)
'''
