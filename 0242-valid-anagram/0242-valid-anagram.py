class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f=0
        if len(s)!=len(t):
            return False
        for i in s:
            if s.count(i)==t.count(i):
                f=1
            else:
                f=0
                return False
        if f==1:
            return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna