#   生成括号
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

# 例如，给出 n = 3，生成结果为：

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution(object):

            
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def generatePa(left,right,pa,res):
            if(left > right or left < 0 or right < 0):
                return
            if(left == 0 and right == 0):
                res.append(pa)
            else:
                if(left > 0):
                    generatePa(left-1,right,pa+'(',res)
                if(right > 0):
                    generatePa(left,right-1,pa+')',res)

        res = []
        pa = ''
        generatePa(n,n,'',res)
        return res
A =Solution()
print(A.generateParenthesis(5))
