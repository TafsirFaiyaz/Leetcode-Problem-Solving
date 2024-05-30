#29. Divide Two Integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        sign = (dividend < 0) == (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)

        currSum = 0
        currentDivisor = divisor
        n = 1

        while dividend >= divisor :

            while dividend >= currentDivisor :

                dividend -= currentDivisor          # Reducing dividend
                currSum += n                        
                n += n                              # Increasing n because I want to accelarate the division by 2x
                currentDivisor += currentDivisor    # To increase the current divisor by 2x to accelarate

            n = 1                            # If current_Divisor gets bigger than dividend the value of n and currentDivisor gets reset
            currentDivisor = divisor
        
        if not sign:                         # If divisor or dividend if one is negative then currSum would be negative
            currSum = -currSum

        MIN = -2147483648
        MAX = 2147483647
        return min(MAX, max(MIN, currSum))
