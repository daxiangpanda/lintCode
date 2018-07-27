class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        remain = n
        lent = 9
        i = 0
        while(remain>=0):
            remain -= lent * 10 ** i * (i+1)
            i+=1
        print(remain + 9 * 10 ** (i-1) * (i))

A = Solution()
print(A.findNthDigit(1000))
print(A.findNthDigit(10))