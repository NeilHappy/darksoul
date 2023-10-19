#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = headA
        B = headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
        """
        d = dict()
        p = headA
        while p != None:
            d[p] = True
            p = p.next
        p = headB
        while p != None:
            if p in d:
                return p
            p = p.next
        return None
        """


# @lc code=end
