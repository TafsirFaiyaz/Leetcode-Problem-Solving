# 506. Relative Ranks

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        x = sorted(score, reverse=True)

        for i in range(len(score)):
            index = x.index(score[i])

            if index == 0:
                score[i] = "Gold Medal"

            elif index == 1:
                score[i] = "Silver Medal"

            elif index == 2 :
                score[i] = "Bronze Medal"

            else:
                score[i] = str(index + 1)

        return score
