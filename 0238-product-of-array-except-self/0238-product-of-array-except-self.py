class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=[0]*len(nums)
        a=1
        for i in range(len(nums)):
            p[i]=a
            a*=nums[i]
        s=[0]*len(nums)
        b=1
        for i in range(len(nums)-1,-1,-1):
            s[i]=b
            b*=nums[i]
        r=[0]*len(nums)
        for i in range(len(nums)):
            r[i]=s[i]*p[i]
        return r




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna