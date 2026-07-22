class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxx = float('-inf')
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
                maxx = max(maxx, count)
            elif s[i] == ')':
                count -= 1
        if maxx == float('-inf'):
            return 0
        return maxx