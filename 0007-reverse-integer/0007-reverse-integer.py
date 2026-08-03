class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        if x<0:
            t=-x
            while t:
                a=t%10
                rev=rev*10+a
                t=t//10
            if rev > 2**31 - 1 or rev <-2**31:
                return 0
            else:
                return -rev
        else:
            while x:
                a=x%10
                rev=rev*10+a
                x=x//10
            if rev>2**31 - 1 or rev<-2**31:
                return 0
            else:
                return rev

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna