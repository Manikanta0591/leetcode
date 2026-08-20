class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        res=[0]*(len(num1)+len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                a=int(num1[i])
                b=int(num2[j])
                mul=a*b
                pos=i+j+1
                total=mul+res[pos]
                res[pos]=total%10
                res[pos-1]+=total//10
        return ''.join(map(str,res)).lstrip('0')

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna