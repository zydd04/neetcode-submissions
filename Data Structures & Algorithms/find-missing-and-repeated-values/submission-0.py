class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        ex_sum = int((n**2)*((1+n**2))/2)
        dup = set()
        d = 0
        real_sum = 0
        for g in grid:
            for num in g:
                real_sum += num
                if num in dup:
                    d = num
                else:
                    dup.add(num)
        m = ex_sum - real_sum + d
        print(d)
        print(ex_sum)
        print(real_sum)
        return [d,m]
        