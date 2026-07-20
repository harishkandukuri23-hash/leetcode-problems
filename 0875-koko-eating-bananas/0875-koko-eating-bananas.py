class Solution:
    def Speed(self,n,piles):
        total=0
        for i in piles:
            total+=(i+n-1)//n
        return total
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans= -1
        while(low<=high):
            mid=low+(high-low)//2
            if(self.Speed(mid,piles)<=h):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
