class Solution:
    def maxScore(self, s: str) -> int:
        l = 0
        score = 0
        maxx = 0
    
        for _ in range(len(s)-1):
            c0 = Counter(s[:l+1])
            c1 = Counter(s[l+1:])
            score = c0["0"] + c1["1"]
            maxx = max(score, maxx)
            l += 1
        return maxx
        