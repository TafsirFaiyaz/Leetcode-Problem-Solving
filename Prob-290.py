#290. Word Pattern

# Each character in the pattern corresponds to a unique word in s.
# The order of the words in s must match the order of the characters in the pattern.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        x = s.split()
        if len(x) != len(pattern):     # order has to be same
            return False

        m = {}
        unique_val = []

        for i in range(len(pattern)):
            if pattern[i] not in m:                # Assigning a unique value for each char in pattern

                if x[i] not in unique_val:         # Making sure the same value is not assigned to another char of pattern
                    m[pattern[i]] = x[i]
                    unique_val.append(x[i])

                else:                              # As one val of x can't be assigned to two different char from pattern
                    return False

            else:
                if m[pattern[i]] != x[i]:           # It means pattern[i] already has a val and it does not match with x[i]. 
                    return False

        return True                                 # Means pattern is the same
        
