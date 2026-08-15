class Solution:
    def kthDigit(self, k: int) -> int:
        if k<=9:
            return k
        k-=9
        l=2
        while True:
            block=9*(10**(l-2))
            digits=block*10*l
            if k<=digits:
                b_start=10**(l-2)
                digits_per=10*l
                b=b_start+(k-1)//digits_per
                rem=(k-1)%digits_per
                idx=rem//l
                digit_idx=rem%l
                if b%2==0:
                    num=10*b+idx
                else:
                    num=10*b+(9-idx)
                return int(str(num)[digit_idx])
            k-=digits
            l+=1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna