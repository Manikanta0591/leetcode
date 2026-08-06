from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        n=len(nums)
        result=[num for num, freq in c.items() if freq > n//3]
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna