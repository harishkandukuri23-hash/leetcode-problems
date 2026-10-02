class Solution(object):
    def subsetsWithDup(self, nums):
        final=[]
        res=[]
        nums.sort()
        def solve(start):
            final.append(res[:])
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                res.append(nums[i])
                solve(i+1)
                res.pop()
        solve(0)
        return final
        