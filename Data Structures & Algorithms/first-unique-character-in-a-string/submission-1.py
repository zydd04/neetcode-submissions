class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for key in counter.keys():
            if counter[key] == 1:
                return s.index(key)
        return -1