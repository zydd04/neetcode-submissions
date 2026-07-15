class Solution:
    def longestPalindrome(self, s: str) -> str:
        string = ''
        for i in range(len(s)):
            r = len(s) - 1
            while(i <= r):
                word = s[i:r+1]
                if (word == word[::-1] and len(word) > len(string)):
                    string = word
                r -= 1
        return string

