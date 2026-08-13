class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k:int)->bool:
            hours=0
            for pile in piles:
                hours+=pile//k
                if pile%k!=0:
                    hours+=1
                if hours>h:
                    return False
            return True
        left,right=1,max(piles)
        ans=right
        while left<=right:
            mid=left+(right-left)// 2
            if canFinish(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna