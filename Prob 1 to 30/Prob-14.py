class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        st=""
        l = strs[0]

        for i in range(len(l)):
            m = l[i]    

            for j in strs:       
                
                if j[i] != m:           #checking if m is present in all the string in the list
                    return st

            st += m
