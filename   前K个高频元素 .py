#   前K个高频元素
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

# 例如，

# 给定数组 [1,1,1,2,2,3] , 和 k = 2，返回 [1,2]。

# 注意：

# 你可以假设给定的 k 总是合理的，1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
import random
import time
class Solution:
    # 方法1：直接遍历数组，依次插入dic，后排序，最后输出，复杂度较高
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,1) + 1
        l = [(item,dic[item]) for item in dic]
        l.sort(key = lambda l:l[1], reverse = True)
        res = []
        for i in range(k):
            res.append(l[i][0])
        return res
    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,1) + 1
        topK = heapq.nlargest(k,dic,key=lambda s:dic[s])
        return topK
        # l = [(item,dic[item]) for item in dic]
        # l.sort(key = lambda l:l[1], reverse = True)
        # res = []
        # for i in range(k):
        #     res.append(l[i][0])
        # return res
A=Solution()
testList = [random.randint(1,1000000) for i in range(1000000)]
# print(testList)

time1 = time.time()
A.topKFrequent(testList,2000)
time2 = time.time()
A.topKFrequent1(testList,2000)
time3 = time.time()
print(time2 - time1)
print(time3 - time2)