class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        count = 1
        counts = []
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1: count += 1
            elif nums[i+1] - nums[i] == 0:
                count = count
            else:
                counts.append(count)
                count = 1
            i += 1
        counts.append(count)
        return max(counts)
