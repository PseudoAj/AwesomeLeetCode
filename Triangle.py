class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        sum=0
        pIdx=0
        for row in triangle:
            if(len(row)==1):
                element=self.getMin(row,0)
            else:
                for j in xrange(len(row)):
                    temp=self.getMin(row,j)
                    if self.isNgh(pIdx,row.index(temp)):
                        element=temp
                        break
            
            sum+=element
        return sum
        
        
    def getMin(self,row,i):
        a=self.msort(row)
        return a[i]
    
    def msort(self,x):
        result = []
        if len(x) < 20:
            return sorted(x)
        mid = int(len(x)/2)
        y = self.msort(x[:mid])
        z = self.msort(x[mid:])
        i = 0
        j = 0
        while i < len(y) and j < len(z):
                if y[i] > z[j]:
                    result.append(z[j])
                    j += 1
                else:
                    result.append(y[i])
                    i += 1
        result += y[i:]
        result += z[j:]
        return result
    
    def isNgh(self,i,j):
        if (j-1==0):
            return True
        elif(j-1==1):
            return True
        else:
            return False
