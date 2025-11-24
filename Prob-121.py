class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = 9999
        profit = 0
        n = len(prices)

        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i] # Update min_price when a new lower price is found

            elif prices[i] > min_price and prices[i] - min_price > profit:   # Update profit if selling at current price yields a higher profit
                profit = prices[i] - min_price

        return profit
        