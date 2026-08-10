class Solution:
    def calPoints(self, o: List[str]) -> int:
        stack=[]
        for i in o:
            if i=="+":
                stack.append(stack[-1]+stack[-2])
            elif i=="D":
                stack.append(stack[-1]*2)
            elif i=="C":
                stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna