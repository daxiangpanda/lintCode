class Solution:
    # 第一种方法 暴力 brute force o(n^3) 时间复杂度
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(s,start,end):
            while(start<=end):
                if(s[start] == s[end]):
                    start+=1
                    end-=1
                    continue
                else:
                    return False
            return True
        
        longest = 0
        sMax = ''
        if(len(s) <= 1):
            return s
        for i in range(len(s)):
            for j in range(i,len(s)):
                if(isPalindrome(s,i,j)):
                    sMax = s[i:j+1] if j-i+1>longest else sMax
                    longest = max(longest,j-i+1)
        
        return sMax
    
    # 第二种方法 中心法 o(n^2)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 寻找以mid为中心的 最长的回文子串的下标
        def findPalindrome(s,mid):
            left = mid - 1
            right = mid + 1
            if(right>=len(s)):
                return mid,mid
            flag = False
            while(s[mid] == s[right]):
                flag = True
                right += 1
                if(right > len(s) - 1):
                    break

            while(left >= 0 and right <= len(s) - 1 and s[left] == s[right]):
                flag = True
                left -= 1
                right +=1
            if(flag):
                return left,right 
            else: 
                return mid,mid
        if(len(s) <= 1):
            return s
        longest = 0
        sMax = ''
        for i in range(len(s)):
            left,right = findPalindrome(s,i)
            print(left)
            print(right)
            if(left == right):
                right+=2
            sMax = s[left+1:right] if right-left+1>longest else sMax
            longest = max(longest,right-left+1)
        return sMax


A = Solution()
print(A.longestPalindrome('ababa'))
        