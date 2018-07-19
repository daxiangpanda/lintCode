#   分类颜色
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

# 注意:
# 不能使用代码库中的排序函数来解决这道题。

# 示例:

# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 进阶：

# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？


# 思想最重要，a,b,c 分别指向最后一个0，1，2的位置，如果再添加0，1，2的话，分别将a,b,c后的值赋成对应的值！不要老是想着交换交换交换！！！！
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = -1
        b = -1
        c = -1
        for i in range(len(nums)):
            print(nums)
            if(nums[i] == 0):
                c+=1
                nums[c]=2
                b+=1
                nums[b]=1
                a+=1
                nums[a]=0
            elif(nums[i] == 1):
                c+=1
                nums[c] = 2
                b+=1
                nums[b] = 1
            elif(nums[i] == 2):
                c+=1
                nums[c] = 2

                
        