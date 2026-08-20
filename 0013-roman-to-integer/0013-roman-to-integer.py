class Solution:
    def romanToInt(self, s: str) -> int:
        t=0
        v={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        for i in range(len(s)):
            if i+1<len(s) and v[s[i]] < v[s[i+1]]:
                t-=v[s[i]]
            else:
                t+=v[s[i]]
        return t


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna