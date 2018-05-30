# 描述
# 设计一种方法，将一个字符串中的所有空格替换成 %20 。你可以假设该字符串有足够的空间来加入新的字符，且你得到的是“真实的”字符长度。

# 你的程序还需要返回被替换后的字符串的长度。
# 如果使用 Java 或 Python, 程序中请用字符数组表示字符串。
# 您在真实的面试中是否遇到过这个题？  是
# 样例
# 对于字符串"Mr John Smith", 长度为 13

# 替换空格之后，参数中的字符串需要变为"Mr%20John%20Smith"，并且把新长度 17 作为结果返回。
# 挑战
# 在原字符串(字符数组)中完成替换，不适用额外空间

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
        for c in range(oldLength-1,0,-1):
            # print(c)
            # print(string[c])

            if(string[c] == ' '):
                # print 1
                k+=1
                for i in range(2):
                    string+='1'
                for d in range(oldLength-1,c,-1):
                    # print(d)

                    print(string)
                    string[d+2] = string[d]
                string[c] = '%'
                string[c+1] = '2'
                string[c+2] = '0'
        # print string
        print(string)
        return len(string)
            

A = Solution()
print(A.replaceBlank(list("hello world"),20))