class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n*(n+1)/2
        acc_sum = sum(nums)
        return int(expected_sum) - acc_sum