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
		print(relationShipMap)
		for i in range(len(c)):
			print(self.isThreeJumps(relationShipMap,c,d))
			# print(relationShipMap,c[i],d[i])

	def isThreeJumps(self,relationShipMap,c,d):
		count = 0
		res = False
		result = []
		for i in range(len(c)):
			if(d[i] in relationShipMap[c[i]]):
				res = True
			else:
				for s1 in relationShipMap[c[i]]:
					if(d[i] in relationShipMap[s1]):
						res = True
					else:
						for s2 in relationShipMap[d[i]]:
							if(d[i] in relationShipMap[s2]):
								res = True
							else:
								continue
			res = False
			result.append(res)
		return result
			

A = Solution()
print(A.withinThreeJumps([1,2],[2,3],[1],[3]))