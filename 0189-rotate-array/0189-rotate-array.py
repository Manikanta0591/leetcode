class Solution:
    def rotate(self, nums: List[int], k: int) -> int:
        k=k%len(nums)
        l=len(nums)-k
        nums[:]=nums[l:]+nums[:l]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna