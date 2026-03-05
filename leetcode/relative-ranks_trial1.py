class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ranks = {}
        rev = sorted(score, reverse = True)

        for i in range(n):
            if i == 0:
                ranks[rev[i]] = "Gold Medal"
            elif i == 1:
                ranks[rev[i]] = "Silver Medal"
            elif i == 2:
                ranks[rev[i]] = "Bronze Medal"
            else:
                ranks[rev[i]] = f"{i + 1}"
        
        return [ranks[s] for s in score]