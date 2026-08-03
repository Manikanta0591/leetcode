class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=[]
        n=len(nums)
        for i in range(n):
            l.append(nums[i])
        for i in range(n):
            l.append(nums[i])
        return l

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna