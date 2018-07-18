class Solution(object):
    def moveList(self,nums,fromIndex,offset):
        for i in range(fromIndex,len(nums)):
            nums[i - offset] = nums[i]
        for i in range(offset):
            nums.pop()
        print(nums)
        
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = j = 0
        if(len(nums) <= 1):
            return nums
        while(True):
            print(nums)
            # print(i)
            offset = 0
            if(i >= len(nums) - 1):
                break
            for j in range(i+1,len(nums)):
                if(j>=len(nums) - 1):
                    self.moveList(nums,i+1,offset)
                    i+=1
                    break
                if(nums[i] == nums[j]):
                    j+=1
                    offset+=1
                else:
                    print(offset)
                    self.moveList(nums,j,offset)
                    i+=1
        print(nums)
        return len(nums)


A = Solution()
# A.moveList([1,1,2],2,1)
print(A.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
