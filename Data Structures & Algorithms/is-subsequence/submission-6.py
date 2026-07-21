class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        f = 0
        for i in range(len(t)):
            if f >= len(s):
                break
            if t[i] == s[f]:
                f += 1
        return f == len(s)
