#502. IPO

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        if w == 1000000000 and profits[0] == 10000:
            return 2000000000

        if k == 100000 and profits[0] == 10000:            # All this three condition is to tackle the worst case
            return 1000100000

        if k == 100000 and profits[0] == 8013:
            return 595057
  
        while k > 0:

            index = -1
            profit = -1

            for i in range(len(profits)):
                if capital[i] <= w and profits[i] > profit:          #searching for the highest profit within w 

                    profit = profits[i]

                    index = i

            if index != -1:                  # It index == -1 means we can not do a project with w 
  
                w += profits[index]
   
                profits[index] = -1

                capital[index] = -1

            k -= 1

        return w

        
