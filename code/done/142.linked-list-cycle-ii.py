# @before-stub-for-debug-begin
from python3problem142 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return None
        slow = head
        fast = head
        while True:
            if not (fast and fast.next):
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return fast


# @lc code=end
