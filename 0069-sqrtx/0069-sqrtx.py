class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l=1
        r=x//2
        while l<=r:
            mid=(l+r)//2
            s=mid*mid
            if s==x:
                return mid
            elif s<x:
                l=mid+1
            else:
                r=mid-1
        return r

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna