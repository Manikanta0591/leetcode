class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string=""
        for i in range(max(len(word1),len(word2))):
            if i <len(word1):
                new_string+=word1[i]
            if i<len(word2):
                new_string+=word2[i]
        return new_string

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna