class Solution(object):
    def maxArea(self, height):
        max_area=0
        l=0
        r=len(height)-1
        while(l < r):
            h=min(height[l],height[r])
            w=r-l
            Area=h*w
            if Area>max_area:
                max_area=Area
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
        