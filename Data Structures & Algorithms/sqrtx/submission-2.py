class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 : return 0
        elif x == 1 : return 1
        high = x // 2
        low = 1
        ans = 1
        while (low <= high) :
            mid = low + (high - low) // 2
            sqr = mid * mid
            if sqr == x:
                return mid
            elif sqr < x:
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
            
        return ans
