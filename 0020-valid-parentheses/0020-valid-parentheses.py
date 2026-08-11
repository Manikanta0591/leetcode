class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash = {')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in hash:
                if stack and stack[-1]==hash[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return not stack

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna