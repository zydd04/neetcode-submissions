class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        out = []
        for char in order:
            if char in count:
                out.append(char * count[char])
                del count[char]  
        for char, freq in count.items():
            out.append(char * freq)

        return "".join(out)

