class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        a=[0]*len(t)
        stack=[]
        for i in range(len(t)):
            while stack and t[i]>t[stack[-1]]:
                j=stack.pop()
                a[j]=i-j
            stack.append(i)
        return a

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna