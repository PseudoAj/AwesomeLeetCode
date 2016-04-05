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
                element=row[0]
            else:
                a=self.msort(row)
                for j in xrange(len(row)):
                    temp=a[j]
                    if self.isNgh(pIdx,row.index(temp)):
                        element=temp
                        pIdx=row.index(temp)
                        break
            print element
            sum+=element
        return sum
        
        
    def getMin(self,row):
        a=self.msort(row)
        return a
    
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
        if (j-i==0):
            return True
        elif(j-i==1):
            return True
        else:
            return False
