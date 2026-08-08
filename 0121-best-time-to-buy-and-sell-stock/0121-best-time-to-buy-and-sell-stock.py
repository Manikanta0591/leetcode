class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=prices[0]
        m=0
        for i in range(len(prices)):
            a=min(a,prices[i])
            m=max(m,prices[i]-a)
        return m


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna