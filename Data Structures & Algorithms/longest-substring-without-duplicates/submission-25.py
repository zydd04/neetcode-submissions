class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        l = 0
        while(l < len(s)):
            r = l + 1
            count = 1
            seen = set()
            seen.add(s[l])
            while(r < len(s)):
                if s[r] not in seen:
                    seen.add(s[r])
                    count += 1
                    r += 1
                else:
                    break
            l += 1
            max_count = max(count, max_count)
        return max_count



                        