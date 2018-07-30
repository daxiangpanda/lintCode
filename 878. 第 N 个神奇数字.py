class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        lcm = self.LCM(A,B)
        small = 0
        big = 20000000000000
        mid = 0
        if(lcm<=1):
            return A+B
        while(small<big):
            mid = (small + big) // 2
            t = mid // A + mid // B - mid // lcm
            if(t>N):
                small = mid+1
            else:
                big = mid
            print(t)
        return mid % 1000000007
    
    def gcd(self,m,n):
        if not n:
            return m
        else:
            return self.gcd(n, m%n)
    def LCM(self,m, n):
        if m*n == 0:
            return 0
        return int(m*n/self.gcd(m, n))
        
A = Solution()
print(A.nthMagicalNumber(1,2,3))
# print(A.nthMagicalNumber(4,2,3))