import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            result=[0]*len(nums)
            if nums.count(0)==1:
                zero_index=nums.index(0)
                nums.remove(0)
                result[zero_index]=math.prod(nums)
            return result
        product=math.prod(nums)
        return [product//i for i in nums]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna