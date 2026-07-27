class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n=len(nums)
        m=nums[0]
        ans=float(-inf)
        for i in range(k,n):
            m=max(m,nums[i-k])
            ans=max(ans,m+nums[i])
        return ans