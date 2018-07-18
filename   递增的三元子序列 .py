
# 给定一个未排序的数组，请判断这个数组中是否存在长度为3的递增的子序列。

# 正式的数学表达如下:

# 如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
# 使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
# 要求算法时间复杂度为O(n)，空间复杂度为O(1) 。

# 示例:
# 输入 [1, 2, 3, 4, 5],
# 输出 true.

# 输入 [5, 4, 3, 2, 1],
# 输出 false.
class Solution:
    # o(n)复杂度 o(1)额外空间
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if(len(nums) < 3):
            return False
        # 两个变量 first代表第一个值，较小的值 second代表中间的值
        # 如果nums中值比first小 那么更新first值为该值
        # 如果有值在first和second之间，那么更新second的值
        # 如果有值比second大，那么return True
        first = float('INF')
        second = float('INF')
        for num in nums:
            if(num<first):
                first = num
            elif(num>first and num<second):
                second = num
            elif(num>second):
                return True
        return False