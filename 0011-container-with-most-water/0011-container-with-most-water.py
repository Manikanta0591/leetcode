class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        max_a=0
        while l<r:
            a=min(height[l],height[r])*(r-l)
            max_a=max(a,max_a)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_a

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna