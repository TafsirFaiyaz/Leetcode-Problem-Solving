#826. Most Profit Assigning Work

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        n = len(profit)
        temp = []

        for i in range(len(worker)):
            temp.append((profit[i],difficulty[i]))
        
        temp.sort(reverse=True)
        worker.sort(reverse=True)

        i = 0
        m = len(worker)
        max_profit = 0
        x = 0

        while i < m:

            for j in range(x,n):
                if worker[i] >= temp[j][1]:
                    max_profit += temp[j][0]
                    x = j
                    break

            i += 1  

        return max_profit
