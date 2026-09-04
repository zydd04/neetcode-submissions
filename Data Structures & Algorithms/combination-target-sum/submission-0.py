class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(i: int, curr: list[int], total: int):
            if total == target:
                ans.append(list(curr))
                return
            if total > target or i >= len(nums):
                return

            curr.append(nums[i])
            backtrack(i, curr, total + nums[i])
            curr.pop()
            backtrack(i+1, curr, total)

        backtrack(0, [], 0)

        return ans