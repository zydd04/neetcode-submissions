class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_w = defaultdict(list)
        map_p = defaultdict(list)
        words = s.split()
        for i, char in enumerate(pattern):
            map_p[char].append(i)
        for i, word in enumerate(words):
            map_w[word].append(i)
        return sorted(map_p.values()) == sorted(map_w.values())