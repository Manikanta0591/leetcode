class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        s=0
        r=len(numbers)-1
        while (l<r):
            s=numbers[l]+numbers[r]
            if s==target:
                return [l+1,r+1]
            if s<target:
                l+=1
            else:
                r-=1
        return []

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna