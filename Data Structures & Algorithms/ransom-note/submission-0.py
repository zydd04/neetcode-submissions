class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = Counter(magazine)
        r = Counter(ransomNote)

        for char, freq in r.items():
            print(f"char: {char}, freq: {freq}")
            if not char in r or freq > m[char]:
                return False
        return True
