class Solution(object):
    def subarraySum(self, nums, k):
        count=0
        current_sum=0
        sum={0:1}
        for i in nums:
            current_sum+=i
            if current_sum-k in sum:
                    count+=sum[current_sum-k]
            sum[current_sum]=sum.get(current_sum,0)+1
        return count