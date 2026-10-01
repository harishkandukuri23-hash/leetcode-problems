class Solution(object):
    def subsets(self, nums):
        f_res = []
        res = []

        def bk(start):
            # base case
            if start == len(nums):
                f_res.append(res[:])
                return

            # not checking
            bk(start + 1)

            # checking
            res.append(nums[start])
            bk(start + 1)
            res.pop()

        bk(0)

        return f_res