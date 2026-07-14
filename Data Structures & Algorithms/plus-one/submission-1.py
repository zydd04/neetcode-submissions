class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = 1
        for i in range(len(digits)):
            digit += 10**(len(digits)-1-i)*digits[i]
        return [int(s) for s in str(digit)]
