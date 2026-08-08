class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        for a in range(len(nums)-2):
            if a!=0 and nums[a]==nums[a-1]:
                continue
            for b in range(a+1,len(nums)-2):
                if b>a+1 and nums[b]==nums[b-1]:
                    continue
                c=b+1
                d=len(nums)-1
                smallest=nums[a]+nums[b]+nums[b+1]+nums[b+2]
                if smallest>target:
                    break
                largest=nums[a]+nums[b]+nums[-1]+nums[-2]
                if largest<target:
                    continue
                while c<d:
                    if nums[a]+nums[b]+nums[c]+nums[d]==target:
                        print(a,b,c,d)
                        ans.append([nums[a],nums[b],nums[c],nums[d]])
                        while c<d and nums[c]==nums[c+1]:
                            c+=1
                        while d>c and nums[d]==nums[d-1]:
                            d-=1
                        c+=1
                        d-=1
                    elif nums[a]+nums[b]+nums[c]+nums[d]>target:
                        d-=1
                    else:
                        c+=1
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna