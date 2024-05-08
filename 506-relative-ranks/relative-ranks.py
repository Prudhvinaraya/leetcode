class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        sorted_score = sorted(score, reverse=True)
        rank_dict = {}
        for i in range(len(sorted_score)):
            if i == 0:
                rank_dict[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                rank_dict[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                rank_dict[sorted_score[i]] = "Bronze Medal"
            else:
                rank_dict[sorted_score[i]] = str(i + 1)

        return [rank_dict[score[i]] for i in range(len(score))]
            