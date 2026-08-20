class Solution:
    def romanToInt(self, s: str) -> int:
        a={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        r=0
        for i in range(len(s)):
            curr=a[s[i]]
            next_val=a[s[i+1]] if i+1<len(s) else 0
            if curr<next_val:
                r-=curr
            else:
                r+=curr
        return r

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna