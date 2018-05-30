class Solution:
    """
    @param n: the given number
    @return: Sum of elements in subsets
    """
    def subSum(self, n):
        # write your code here
        return self.PowerSetsRecursive2(range(1,n+1))
 
    def PowerSetsRecursive2(self,items):  
        # the power set of the empty set has one element, the empty set  
        result = [[]]  
        for x in items:  
            result.extend([subset + [x] for subset in result]) 
        # print(result)
        res = 0 
        for i in result:
        	res+=sum(i)
        return res  

A = Solution()
for i in range(1,100):
	print(str(i)+'    '+str(A.subSum(i)))


# math problem