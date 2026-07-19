class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxx = 0
        count = defaultdict(int)
        maxx_l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxx = max(count[s[r]], maxx) 
            if r - l + 1 > maxx + k:
                count[s[l]] -= 1
                l += 1
            maxx_l = max(maxx_l, r - l + 1)
        return maxx_l

