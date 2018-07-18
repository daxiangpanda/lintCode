# 字典树是个啥（trie Tree）
# 使用字典树并不会快
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs) == 0):
            return ""
        if(len(strs) == 1):
            return strs[0]
        firstLen = len(strs[0])
        res = ""
        for idx in range(firstLen):
            ch = strs[0][idx]
            for str in strs:
                if(idx>=len(str)):
                    return res
                if(str[idx] == ch):
                    continue
                else:
                    return res
            res+=ch
        return res
                
A =Solution()
print(A.longestCommonPrefix(["flower","flow","flight"]))