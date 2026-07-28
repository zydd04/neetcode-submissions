class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        c = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            
            if nums[i] > nums[i-1]:
                c += nums[i]
            else:
                c = nums[i]
            res = max(c, res)
            print(f"num: {nums[i]}, num before: {nums[i-1]}, couunt: {c}, max: {res}")
        return res

