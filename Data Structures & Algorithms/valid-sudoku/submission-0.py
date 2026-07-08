class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j].isdigit():
                    k = (i // 3) * 3 + (j // 3)
                    if board[i][j] not in nums.keys():
                        nums[board[i][j]] = [[i , j, k]]
                    else:
                        for row, col, box in nums[board[i][j]]:
                            if row == i or col == j or box == k:
                                return False
                            
                        (nums[board[i][j]]).append([i, j, k])
        return True

