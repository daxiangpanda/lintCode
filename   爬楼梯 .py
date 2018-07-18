class Solution:
    res = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 1):
            self.res[1] = 1
            return 1
        if(n == 2):
            self.res[2] = 2
            return 2
        if(n<1):
            return 0
        if(n in self.res):
            return self.res[n]
        self.res[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.res[n]

A = Solution()
print(A.climbStairs(35))