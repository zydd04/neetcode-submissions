class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ''
        o = 0
        p = 0
        n = len(word1)
        m = len(word2)
        f = min(n, m)
        for i in range(2*f):
            if i % 2 == 0:
                word += word1[o]
                o += 1
            else:
                word += word2[p]
                p += 1
        word += word1[f:] + word2[f:]
        return word