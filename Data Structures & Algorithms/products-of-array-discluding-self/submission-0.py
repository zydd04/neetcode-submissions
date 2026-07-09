class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        for i in range(len(nums)):
            prefix_l = nums[0:i]
            suffix_l = nums[i+1:]
            prefix = 1
            suffix = 1
            for o in range(len(prefix_l)):
                prefix *= prefix_l[o]
            for j in range(len(suffix_l)):
                suffix *= suffix_l[j]
            product.append(suffix*prefix)
        return product