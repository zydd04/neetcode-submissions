class Solution:
    def reverse(self, x: int) -> int:
        num = (str(x)[::-1])
        if num[len(num)-1] == "-":
            num = - int(num[0:len(num)-1])
        if int(num) > 2**31 - 1 or int(num) < -2**31:
            return 0
        return int(num) 