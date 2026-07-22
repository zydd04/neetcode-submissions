class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        v = 0
        for i in range(len(s)):
            if len(t) == v:
                break
            if s[i] == t[v]:
                v += 1
        return len(t) - v