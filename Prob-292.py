class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0 
        # If there are 4 stones, no matter if you take 1, 2, or 3 stones,
        # your opponent can take the remaining stones and win. Thus, you lose if the initial number of stones is a multiple of 4.   
        # For any other number of stones, you can always make a move that leaves a multiple of 4 for your opponent, ensuring your victory.
        # suppose there is 5 stones, you can take 1 stone and leave 4 stones for your opponent.
        # similarly, if there are 6 stones, you can take 2 stones and leave 4 stones for your opponent.
        # if there are 7 stones, you can take 3 stones and leave 4 stones for your opponent.
        # Therefore, the winning strategy is to always leave a multiple of 4 stones for your opponent.