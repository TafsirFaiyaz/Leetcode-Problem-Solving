#7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:

            y = int(str(x)[:0:-1]) * -1

        else:
            y = int(str(x)[::-1])

        if y> 2147483647 or y < -2147483648:
            return 0

        return y

