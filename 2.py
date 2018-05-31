import math
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        countOfTwo = 0
        countOfFive = 0
        countOfZero = 0
        for i in range(1,n+1):
        	if(i%10 == 2):
        		k = i
        		# print('k'+str(k))
        		# print()
        		# countOfTwo+=1
        		while(k>0):
        			if(k%2==0 and k//10!=0):
        				countOfTwo+=1
        				# print('k'+str(k))
        			k//=2
        	if(i%10 == 5):
        		k=i
        		# countOfFive+=1
        		while(k>0):
        			if(k%5==0 and k//10!=0):
        				countOfFive+=1
        			k//=5
        	if(i%10 == 0):
        		print(math.log(i,10))
        		countOfZero+=math.floor(math.log(i,10))
        print(countOfTwo)
        print(countOfFive)
        print(countOfZero)
        factorial = 1
        return min(countOfTwo,countOfFive) + countOfZero

A = Solution()
print(A.trailingZeros(11))

# 0000 0000 0000 0000 0000 0000 0