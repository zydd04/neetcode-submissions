class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        count = 0
        for i in range(len(nums)):
            if not nums[i] in seen:
                seen.add(nums[i])
            else:
                count += 1
                nums[i] = float('inf')
        nums.sort()
        return len(nums) - count
        