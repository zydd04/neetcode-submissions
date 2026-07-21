class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = min(strs, key=len)
        for i in range(len(pre)):
            for s in strs:
                if not s[i] == pre[i]:
                    return pre[:i]
        return pre