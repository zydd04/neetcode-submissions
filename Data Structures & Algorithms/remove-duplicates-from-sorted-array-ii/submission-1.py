class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = defaultdict(int)
        dup = 0
        for i in range(len(nums)):
            count[nums[i]] += 1
            if count[nums[i]] > 2:
                nums[i] = float('inf')
                dup += 1
        nums.sort()
        return len(nums) - dup