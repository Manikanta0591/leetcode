class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum=0
        d={}
        d[0]=1
        s=0
        for i in range(len(nums)):
            curr_sum += nums[i]
            required = curr_sum-k
            if required in d:
                s+=d[required]
            if curr_sum not in d:
                d[curr_sum]=1
            else:
                d[curr_sum]+=1
        return s

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna