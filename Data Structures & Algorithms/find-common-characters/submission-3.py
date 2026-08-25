class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c0 = Counter(words[0])
        miss = set()
        for word in words[1:]:
            c1 = Counter(word)
            for char, freq in c0.items():
                if char in c1.keys():
                    if freq > c1[char]:
                        c0[char] = c1[char]
                else:
                    miss.add(char)
                    
        
        ans = []
        for char, freq in c0.items():
            if char not in miss: 
                for _ in range(freq):
                    ans.append(char)
        return ans

            