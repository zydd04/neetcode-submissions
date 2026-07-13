class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for matrice in matrix:
            h = len(matrice) - 1
            l = 0
            while(l <= h):
                mid = l + (h-l)//2
                if matrice[mid] == target: return True
                elif matrice[mid] < target: l = mid + 1
                else: h = mid - 1
        return False