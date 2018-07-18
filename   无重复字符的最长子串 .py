class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 记录最大长度
        maxLength = 0
        # 记录当前子串的长度
        temp = 0
        # 记录字母以及该字母上次出现的序号的dic
        alphabetDic = {}
        for i in range(len(s)):
            # 出现新的字母了
            if(not s[i] in alphabetDic):
                temp+=1
                alphabetDic[s[i]] = i
            else:
                # 如果出现过的字母再次出现，那么如果上次出现该字母的序列在当前子串范围外，不做操作，子串长度加一
                if(alphabetDic[s[i]] + temp <i):
                    temp+=1
                else:
                # 如果上次出现该字母的下标在当前子串内，更新子串长度，并更新最大值长度
                    maxLength = max(temp,maxLength)
                    temp = i - alphabetDic[s[i]]
                # 更新dic
                alphabetDic[s[i]] = i
        # 如果maxLength一直没有被更新，此时再更新一次最大值
        maxLength = max(maxLength,temp)
        return maxLength
