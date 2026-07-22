class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        word_v = {}
        ans = []
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                word_v[i] = 1
            else:
                word_v[i] = 0
        for q in queries:
            tot = 0
            for i in range(q[0], q[1]+1):
                tot += word_v[i]
            ans.append(tot)
        return ans