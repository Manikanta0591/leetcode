class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        left = 0
        right = len(s) - 1
        while s[left] == s[right]:
            left+=1
            right-=1

        return s[left:right] == s[left:right][::-1] or s[left+1:right+1] == s[left+1:right+1][::-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna