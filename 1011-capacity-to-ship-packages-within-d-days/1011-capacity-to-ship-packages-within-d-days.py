class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canship(capacity:int)->bool:
            d=1
            curr=0
            for w in weights:
                if curr+w>capacity:
                    d+=1
                    curr=0
                curr+=w
                if d>days:
                    return False
            return True
        l=max(weights)
        r=sum(weights)
        ans=0
        while l<=r:
            mid=(l+r)//2
            if canship(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna