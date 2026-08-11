class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        stack=[]
        for i in a:
            while stack and i<0<stack[-1]:
                if -i>stack[-1]:
                    stack.pop()
                    continue
                elif -i==stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(i)
        return stack

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna