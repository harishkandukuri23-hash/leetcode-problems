class Solution(object):
    def mySqrt(self, x):
        l=0
        h=x
        ans=-1
        while(l<=h):
            m=(l+h)//2
            if (m*m<=x):
                ans=m
                l=m+1
            else:
                h=m-1
        return ans