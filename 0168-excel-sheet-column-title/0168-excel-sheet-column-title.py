class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        r=""
        while columnNumber>0:
            columnNumber-=1
            remainder=columnNumber%26
            r=chr(ord('A')+remainder)+r
            columnNumber//=26
        return r

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna