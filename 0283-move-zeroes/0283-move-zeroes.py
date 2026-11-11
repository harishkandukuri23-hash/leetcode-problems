class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l=0
        r=len(nums)
        for i in range(r):
            if nums[i]!=0:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
        return nums


        