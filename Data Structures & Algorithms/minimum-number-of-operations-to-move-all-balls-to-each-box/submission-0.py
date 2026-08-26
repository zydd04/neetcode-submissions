class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []

        for i in range(len(boxes)):
            t = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    t += abs(j - i)
            ans.append(t)
        
        return ans