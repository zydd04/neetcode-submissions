class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        maxArea = 0
        while(l < len(heights) - 1):
            r = len(heights) - 1
            while(l < r):
                area = min(heights[l], heights[r])*(r - l) 
                if(area > maxArea): maxArea = area
                r -= 1
            l += 1
        return maxArea