
# 编写一个程序，找到两个单链表相交的起始节点。

 

# 例如，下面的两个链表：

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# 在节点 c1 开始相交。

 

# 注意：

# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 0
        lenB = 0
        lA = headA
        lB = headB
        while(not lA == None):
            lenA+=1
            lA = lA.next
        while(not lB == None):
            lenB+=12
            lB = lB.next
        
        p = headA
        q = headB
        if(lenA>lenB):
            for i in range(lenA-lenB):
                p = p.next
            if(p == q):
                return True
        else:
            for i in range(lenB-lenA):
                q = q.next
            if(p == q):
                return True
        return False