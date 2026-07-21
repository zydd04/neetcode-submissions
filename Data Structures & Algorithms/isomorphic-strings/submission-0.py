class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = defaultdict(list)
        map_t = defaultdict(list)
        for i, char in enumerate(s):
            map_s[char].append(i)
        for i, char in enumerate(t):
            map_t[char].append(i)
        return sorted(map_s.values()) == sorted(map_t.values())
