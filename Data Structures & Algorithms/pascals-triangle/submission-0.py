class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            row = [1]
            prev = result[i-1]
            for j in range(1, i):
                row.append(prev[j-1]+prev[j])
            row.append(1) 
            result.append(row)   
        return result