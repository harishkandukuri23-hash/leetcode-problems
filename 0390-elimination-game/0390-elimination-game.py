class Solution:
    def lastRemaining(self, n: int) -> int:
        start=1
        diff=1
        is_left=True
        while n>1:
            if not( n%2==0  and is_left==False):
                start=start+diff
            n=n//2
            diff=diff*2
            is_left= not is_left
        return start
        
                
