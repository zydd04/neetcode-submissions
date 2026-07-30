class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s2) - 1
        check = ''
        for l in range(len(s2)-len(s1)+1):
            if s2[l] in s1:
                r = l + len(s1) - 1
                while (l <= r):
                    check += s2[r]
                    r -= 1
                if sorted(check) == sorted(s1):
                    return True
                else:
                    check = ''
        return False