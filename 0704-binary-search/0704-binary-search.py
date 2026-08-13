class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==t:
                return mid
            elif nums[mid]<t:
                l=mid+1
            else:
                r=mid-1
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna