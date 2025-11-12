#3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        max = 0
        for i in range(N):
            m = s[i]

            for j in range(i+1,N):
                if s[j] not in m:          # Checking if any charecter is repeating
                    m += s[j]

                else:
                    break
            
            if max < len(m):            
                max = len(m)

        return max

            
        
