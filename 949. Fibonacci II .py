class Solution:
    """
    @param n: an integer
    @return: return a string
    """
    def lastFourDigitsOfFn(self, n):
        # write your code here
        return self.mode(0,1,1,1,n-1,10000)

    def mode(self,a0,a1,a2,a3,b,mode):
        sum3 = 1%mode
        sum2 = 1%mode
        sum1 = 1%mode
        sum0 = 0%mode

        while(b>0):
            if(b%2 == 1):
                b3 = (sum2 * a1 + sum3 * a3)%mode
                b2 = (sum2 * a0 + sum3 * a2)%mode
                b1 = (sum0 * a1 + sum1 * a3)%mode
                b0 = (sum0 * a0 + sum1 * a2)%mode
                sum3,sum2,sum1,sum0 = b3,b2,b1,b0
                # sum = (sum*a)%mode
            b//=2
            b3 = (a2 * a1 + a3 * a3)%mode
            b2 = (a2 * a0 + a3 * a2)%mode
            b1 = (a0 * a1 + a1 * a3)%mode
            b0 = (a0 * a0 + a1 * a2)%mode
            a3,a2,a1,a0 = b3,b2,b1,b0
        return str(sum2)

A = Solution()
print(A.lastFourDigitsOfFn(9))