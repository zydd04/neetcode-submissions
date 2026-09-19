class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        summ = 0
        while (summ != 1):
            summ = 0
            while (n > 0):
                summ += (n % 10)**2
                n //= 10
            n = summ
            if summ in seen:
                return False
            else: seen.add(summ) 

        return True
        
        