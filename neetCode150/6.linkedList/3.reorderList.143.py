# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity: O(n)
# Space Complexity: O(1)
# 30 minutes
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head

        while(fast and fast.next):
          slow = slow.next
          fast = fast.next.next
        
        prev = None

        while(slow):
          nxt = slow.next
          slow.next = prev
          prev = slow
          slow = nxt

        curr = head

        while(prev.next):
          currNxt = curr.next
          prevNxt = prev.next

          curr.next = prev
          curr = currNxt

          prev.next = curr
          prev = prevNxt










"""

Create reversed Linked list

Connect original list to reversed list until curr.val === reversed.val


"""
