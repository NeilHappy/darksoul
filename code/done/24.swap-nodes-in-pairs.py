#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            first = cur.next
            third = cur.next.next.next

            cur.next = first.next
            cur.next.next = first
            first.next = third
            cur = cur.next.next
        return dummy.next

# @lc code=end
