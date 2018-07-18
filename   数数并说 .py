class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        for i in range(n):
            if len(res) == 0:
                res.append(1)
                continue
            res.append(self.read(res[-1]))
        print(res)
        return res
    def read(self,n):
        s = str(n)
        offset = 1
        res = ''
        if(n == 1):
            return 11
        for i in range(len(str(n))-1):
            if(s[i] == s[i+1]):
                offset += 1
                if(i+1 == len(s) -1):
                    res += str(offset)
                    res += str(s[i])
                    break
                continue
            else:

                res += str(offset)
                res += str(s[i])
                offset = 1
                if(i+1 == len(s) -1):
                    res += str(offset)
                    res += str(s[i+1])
                    break
        return int(res)

A = Solution()
print(A.countAndSay(50))