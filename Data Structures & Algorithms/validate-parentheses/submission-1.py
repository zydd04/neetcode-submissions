class Solution:
    def isValid(self, s: str) -> bool:
        op = ['(', '{', '[']
        cl = [')', '}', ']']
        stack = []

        for i in range (len(s)): 
            if (s[i] in op):
                stack.append(s[i])
            elif(s[i] in cl):
                if len(stack) > 0 and (s[i] == ')'and stack[-1] == '(' or s[i] == '}'and stack[-1] == '{' or s[i] == ']'and stack[-1] == '['):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0