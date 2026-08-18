from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str)->str:
        if not s or not t or len(s)<len(t):
            return ""
        need=Counter(t)
        window={}
        have=0
        required=len(need)
        left=0
        best_start=0
        best_length=float("inf")
        for right,char in enumerate(s):
            window[char]=window.get(char,0)+1
            if char in need and window[char]==need[char]:
                have+=1
            while have==required:
                current_length=right-left+1
                if current_length<best_length:
                    best_start=left
                    best_length=current_length
                left_char=s[left]
                window[left_char]-=1
                if left_char in need and window[left_char]<need[left_char]:
                    have-=1
                left+=1
        if best_length==float("inf"):
            return ""
        return s[best_start:best_start + best_length]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna