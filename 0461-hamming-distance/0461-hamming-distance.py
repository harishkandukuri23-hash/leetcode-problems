class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count=0
        res=x^y
        return res.bit_count()
