class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=set()
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while(l<r):
                t=nums[i]+nums[l]+nums[r]
                if t==0 :
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif t<0 :
                    l+=1
                else:
                    r-=1

        return [list(x) for x in res]
