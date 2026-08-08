class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        st,end=0,len(people)-1
        boat=0
        while st<=end:
            if people[st]+people[end]<=limit:
                st+=1
                boat+=1
                end-=1
            else:
                end-=1
                boat+=1
        return boat

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna