
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

# 示例:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.



class Solution:
    # 方法1 直接深度搜索 缺点：需要一个辅助矩阵来记录是否被访问过
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """        
        row = len(board)
        col = len(board[0])
        visited = [[False] * col  for i in range(row)]
        print(visited)
        def dfs(board,row,col,index,word):
            print(row)
            print(col)
            # print(board[row][col])
            print(visited)
            if(len(word) == index):
                return True
            print('index:'+str(index)+':'+word[index])
            if(row<0 or col<0 or row>= len(board) or col >= len(board[0])):
                return False
            if(not visited[row][col]):
                if(word[index] == board[row][col]):
                    visited[row][col] = True
                    res = dfs(board,row-1,col,index+1,word) or dfs(board,row+1,col,index+1,word) or dfs(board,row,col+1,index+1,word) or dfs(board,row,col-1,index+1,word)
                    visited[row][col] = False
                    return res
            return False
        

        for i in range(row):
            for j in range(col):
                if(dfs(board,i,j,0,word)):
                    return True
        return False
    # 方法2 直接在原矩阵上进行修改 不需要辅助矩阵
    def exist1(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """        
        row = len(board)
        col = len(board[0])
        # visited = [[False] * col  for i in range(row)]
        # print(visited)
        def dfs(board,row,col,index,word):
            print(row)
            print(col)
            # print(board[row][col])
            # print(visited)
            if(len(word) == index):
                return True
            print('index:'+str(index)+':'+word[index])
            if(row<0 or col<0 or row>= len(board) or col >= len(board[0])):
                return False
            
            ch = word[index]
            if(board[row][col] != '+'):
                if(ch == board[row][col]):
                    c = board[row][col]
                    board[row][col] = '+'
                    res = dfs(board,row-1,col,index+1,word) or dfs(board,row+1,col,index+1,word) or dfs(board,row,col+1,index+1,word) or dfs(board,row,col-1,index+1,word)
                    board[row][col] = c
                    return res
            return False
        

        for i in range(row):
            for j in range(col):
                if(dfs(board,i,j,0,word)):
                    return True
        return False
board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]

A = Solution()
print(A.exist(board,"ABCCED"))