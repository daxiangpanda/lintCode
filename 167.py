# 描述
# 你有两个用链表代表的整数，其中每个节点包含一个数字。数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。写出一个函数将两个整数相加，用链表形式返回和。
# 您在真实的面试中是否遇到过这个题？  是
# 样例
# 给出两个链表 3->1->5->null 和 5->9->2->null，返回 8->0->8->null

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        # write your code here
        if(l1 == None):
            return l2
        if(l2 == None):
            return l1
        l = ListNode(0)
        p = l
        jinwei = 0
        while(l1 != None and l2 != None):
            # print l1.val
            # print l2.val
            l.val = l1.val + l2.val + jinwei
            jinwei = 0
            if(l.val >= 10):
                l.val %= 10
                jinwei = 1
            l1 = l1.next
            l2 = l2.next
            if(l1 == None or l2 == None):
                break
            l.next = ListNode(0)
            l = l.next
        if(l1 == None and l2 == None):
            if(jinwei>0):
                l.next = ListNode(jinwei)
            return p
        if(l1 == None):
            if(jinwei == 1):
                l.next = ListNode(0)
                l.next.val = l2.val+jinwei
                if(l.next.val == 10):
                    l.next.val = 0
                    l.next.next = ListNode(0)
                    l.next.next.val = 1
                else:
                    l.next.next = l2.next
            else:
                l.next = l2
        if(l2 == None):
            if(jinwei == 1):
                l.next = ListNode(0)
                l.next.val = l1.val+jinwei
                if(l.next.val == 10):
                    l.next.val = 0
                    l.next.next = ListNode(0)
                    l.next.next.val = 1
                else:
                    l.next.next = l1.next
            else:
                l.next = l1
        return p
    def judeg(self):
        l1 = ListNode(9)
        l1.next = ListNode(9)
        l2 = ListNode(9)
        k = self.addLists(l1,l2)
        while(k):
        	print(k.val)
        	k = k.next
        print(self.addLists(l1,l2))

A = Solution()
A.judeg()