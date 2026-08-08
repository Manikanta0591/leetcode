class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        a=[]
        for i in range(len(arr)):
            a.append((abs(x-arr[i]),arr[i]))
        a.sort()
        r=[]
        for i in range(k):
            r.append(a[i][1])
        r.sort()
        return r

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna