class Solution(object):
    def removeDuplicates(self, nums):
        p = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[p]:
                p += 1
                nums[p] = nums[i]
        return p+1
        