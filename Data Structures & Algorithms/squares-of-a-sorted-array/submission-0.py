class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        for s in nums:
            squares.append(s**2)
        return sorted(squares)