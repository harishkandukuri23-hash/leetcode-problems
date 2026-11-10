class Solution:
    def maxArea(self, height: list[int]) -> int:
        m=0
        l=0
        r=len (height)-1
        while (l<r):
            h=min(height[l],height[r])
            w=r-l
            area=h*w
            if area > m:
                m=area
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return m