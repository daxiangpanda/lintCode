class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n<0):
            return 0
        elif(n == 0 or n == 1):
            return 1
        else:
            for i in range(2,n+1):
                resI = 0
                for j in range(i+1):
                    resI+=(self.numTrees(i-j) * self.numTrees(j))
                
        return result

A = Solution()
print(A.numTrees(19))