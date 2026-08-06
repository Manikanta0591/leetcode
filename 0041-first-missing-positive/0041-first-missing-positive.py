class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set()
        for i in nums:
            if i not in s and i>0:
                s.add(i)
        for i in range(len(s)+1):
            if i+1 not in s:
                return i+1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna