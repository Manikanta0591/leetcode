class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            strs.sort()
            s1=strs[0]
            s2=strs[len(strs)-1]
            a=""
            for ch in range(len(s1)):
                if s1[ch]==s2[ch]:
                    a+=s1[ch]
                else:
                    return a
            return a

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna