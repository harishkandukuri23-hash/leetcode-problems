class Solution(object):
    def generate(self, numRows):
        res=[]
        for i in range(0,numRows):
            lst=[]
            for j in range(i+1):
                if(j==0 or j==i):
                    lst.append(1)
                else:
                    sum=res[i-1][j-1] + res[i-1][j]
                    lst.append(sum)
            res.append(lst)
        return res   