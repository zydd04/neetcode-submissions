class Solution:
    def hammingWeight(self, n: int) -> int:
        num = bin(n)
        c = Counter(num)
        print(c)
        return c['1']