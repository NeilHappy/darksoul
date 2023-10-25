#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
        """
        def reverse(cur: ListNode, pre: ListNode) -> ListNode:
            if cur is None:
                return pre
            next = cur.next
            cur.next = pre
            return reverse(next, cur)
        return reverse(head, None)

# @lc code=end
