
# 描述控制台
# 13. Implement strStr()

# 对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。

# 样例

# 如果 source = "source" 和 target = "target"，返回 -1。

# 如果 source = "abcdabcdefg" 和 target = "bcd"，返回 1。

# 挑战

# O(n2)的算法是可以接受的。如果你能用O(n)的算法做出来那更加好。（提示：KMP）


class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        # write your code here
        res = -1

        if(source == None or target == None or len(source) == 0):
            return -1
        if(len(target) == 0):
            return 0
        for i in range(len(source)):
            state = False
            for j in range(len(target)):
                if(source[i+j]==target[j]):
                #     print(source[i+j])
                #     print(target[j])
                    if(j==len(target)-1):
                        res = i

                        state = True
                    else:
                        # i+=1
                        continue
                else:
                    break
            if(state==True):
                break
                # state = True
            # res = i
            # break
        return res


A = Solution()
print(A.strStr('abcdabcdefg','bcd'))