class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0]*len(temperatures)
        temps = []
        for i,tmp in enumerate(temperatures):
            while temps and tmp > temperatures[temps[-1]]:
                prev = temps.pop()
                out[prev] = i - prev
            temps.append(i)
        return out


        





       