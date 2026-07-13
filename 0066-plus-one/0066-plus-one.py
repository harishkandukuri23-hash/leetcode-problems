class Solution(object):
    def plusOne(self, digits):
        cary=1
        for i in range(len(digits)-1,-1,-1):
            sum=digits[i]+cary
            digits[i]=sum%10
            cary=sum/10
        if cary==1:
            digits.insert(0,1)
        return digits