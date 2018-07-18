class Solution(object):
    def isLetter(self,letter):
        if((ord(letter) >= ord('a') and ord(letter)<= ord('z')) or (ord(letter) >= ord('A') and ord(letter)<= ord('Z'))):
           return True
        else:
           return False
    def isNum(self,letter):
        if(ord(letter) >= ord('0') and ord(letter)<= ord('9')):
           return True
        else:
           return False
                                                                    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(len(s) == 0) :
            return Ture
        i = 0
        j = len(s) - 1

        while(i<=j):
            if((not self.isLetter(s[i])) and (not self.isNum(s[i]))):
                i+=1
                continue
            if((not self.isLetter(s[j])) and (not self.isNum(s[j]))):
                j-=1
                continue
            if(self.isLetter(s[i])):
                if((s[i] == chr(ord(s[j]) - 32)) or (s[i] == chr(ord(s[j]) + 32)) or (s[i] == s[j])):
                    i+=1
                    j-=1
                else:
                    return False
            
            elif(self.isNum(s[i])):
                if(s[i] == s[j]):
                    i+=1
                    j-=1
                else:
                    return False
        return True

A = Solution()
print(A.isPalindrome("A man, a plan, a canal: Panama"))
                
           
        