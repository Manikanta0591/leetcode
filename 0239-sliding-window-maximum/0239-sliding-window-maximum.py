class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=[]
        ans=[]
        for i in range(len(nums)):
            while q and q[0]<=i-k:
                q.pop(0)
            while q and nums[q[-1]]<=nums[i]:
                q.pop()
            q.append(i)
            if i>=k-1:
                ans.append(nums[q[0]])
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna