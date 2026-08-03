class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set(nums)
        n=len(s)
        if n<len(nums):
            return True
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna