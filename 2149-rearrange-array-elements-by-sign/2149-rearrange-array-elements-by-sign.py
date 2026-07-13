class Solution(object):
    def rearrangeArray(self, nums):
        res=[0]*len(nums)
        pos=0
        neg=1
        for i in range(0,len(nums)):
            if nums[i]>0:
                res[pos]=nums[i]
                pos+=2
            else:
                res[neg]=nums[i]
                neg+=2
        return res