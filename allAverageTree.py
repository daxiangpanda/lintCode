
# 95. 不同的二叉搜索树 II
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if(n<0):
            return None
        return self.calculateTree(1,n)
    
    def calculateTree(self,left,right):
        treeList = []
        if(left > right):
            treeList.append(None)
            return treeList
        for i in range(left,right+1):
            lTree = self.calculateTree(left,i-1)
            rTree = self.calculateTree(i+1,right)
            for l in lTree:
                for r in rTree:
                    treeNode = TreeNode(i)
                    treeNode.left = l
                    treeNode.right = r
                    treeList.append(treeNode)
        return treeList

A = Solution()
for  i in A.calculateTree(1,3):
    for node in i:
        print(node)
    print()