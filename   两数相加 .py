#   两数相加
# 给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。

# 示例：

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(not l1):
            return l2
        if(not l2):
            return l1
        m = l1,n = l2
        h = ListNode(0)
        res = h
        offset = 0
        while(m != None and n != None):
            add = m.val+n.val+offset
            q = ListNode(add%10)
            h.next = q
            h = h.next
            offset = add / 10
            m = m.next
            n = n.next
        if(m == None and n!= None):
            while(n!=None):
                add = n.val + offset
                q = ListNode(add % 10)
                h.next = q
                h = h.next
                n = n.next
                offset = add / 10
        if(m != None and n== None):
            while(m!=None):
                add = m.val + offset
                q = ListNode(add % 10)
                h.next = q
                h = h.next
                m = m.next
                offset = add / 10
        if(m == None and n == None):
            if(offset == 1):
                add = 1
                q = ListNode(add)
                h.next = q
                h = h.next
        return res.next
            
            

        