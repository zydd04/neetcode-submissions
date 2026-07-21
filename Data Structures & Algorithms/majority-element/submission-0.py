class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter  = Counter(nums)
        for key in counter.keys():
            if counter[key] > len(nums)/2:
                return key