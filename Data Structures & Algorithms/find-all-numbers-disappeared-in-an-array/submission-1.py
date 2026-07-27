class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ex_nums = []

        for i in range(1, len(nums)+1):
            if i not in nums:
                ex_nums.append(i)
        return ex_nums
