class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """
    def replaceBlank(self, string, length):
        # write your code here
        res = ""
        # print string
        oldLength = len(string)
        blankLenth = 0
        length = 0
        for i in string:
            if(i == ' '):
                length+=3
                blankLenth+=1
            else:
                length+=1
        # print res
        k = 0
        for c in range(oldLength-1,-1,-1):
            # print(c)
            # print(string[c])

            if(string[c] == ' '):
                # print 1
                k+=1
                for i in range(2):
                    string+='1'
                for d in range(oldLength-1+(k-1)*2,c,-1):
                    # print(d)

                    print(string)
                    string[d+2] = string[d]
                string[c] = '%'
                string[c+1] = '2'
                string[c+2] = '0'
        # print string
        # print(string)
        return len(string)
            

A = Solution()
print(A.replaceBlank(list("hello  world"),20))