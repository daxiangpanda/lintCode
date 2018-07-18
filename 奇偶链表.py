#   奇偶链表
# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

# 示例 1:

# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
# 示例 2:

# 输入: 2->1->3->5->6->4->7->NULL 
# 输出: 2->3->6->7->1->5->4->NULL
# 说明:

# 应当保持奇数节点和偶数节点的相对顺序。
# 链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 这题主要就是细心！
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        even = head
        if(not even):
            return head
        odd = head.next
        if(not even or not odd):
            return head
        while(odd.next != None):
            # self.pri(head)
            startOdd = even.next
            nextEven = odd.next
            even.next = nextEven
            if(nextEven.next == None):
                nextEven.next = startOdd
                odd.next = None
                break
            odd.next = nextEven.next
            nextEven.next = startOdd
            even = even.next
            odd = odd.next
        return head
    def pri(self,head):
        n = head
        while(n!=None):
            print(n.val)
            n = n.next