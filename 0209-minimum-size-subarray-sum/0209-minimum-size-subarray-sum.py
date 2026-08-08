class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_s=float("inf")
        l,s=0,0
        for i in range(len(nums)):
            if nums[i]==target:
                min_s=1
            s+=nums[i]
            while s>=target:
                min_s= min(min_s, i-l+1)
                s-= nums[l]
                l+=1
        return 0 if min_s == float("inf") else min_s

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna