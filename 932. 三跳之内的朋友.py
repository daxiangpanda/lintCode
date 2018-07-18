class Solution:
	"""
	@param a: The a tuple
	@param b: The b tuple
	@param c: the c tuple
	@param d: the d tuple
	@return: The answer
	"""
	def withinThreeJumps(self, a, b, c, d):
		# Write your code here
		relationShipMap = {}
		for i in range(len(a)):
			if(a[i] in relationShipMap):
				relationShipMap[a[i]].append(b[i])
			else:
				relationShipMap[a[i]] = [b[i]]

		for i in range(len(c)):
			relationShipMap,c[i],d[i]

	def isThreeJumps(self,relationShipMap,c,d):
		count = 0
		res = False
			if(d in relationShipMap[c]):
				res = True
			else:
    			for d1 in relationShipMap[c]:
					if(d in relationShipMap[d1]):
    					res = True
					else:
    					for d2 in relationShipMap[d1]:
    						if(d in relationShipMap[d2]):
    							res = True
							else:
    							continue	
			

A = Solution()
print(A.withinThreeJumps([1,2],[2,3],[1],[3]))