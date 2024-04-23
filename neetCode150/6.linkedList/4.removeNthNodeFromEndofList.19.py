# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity: O(n)
# Space Complexity: O(1)
# 10 minutes
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

      curr = head
      prev = None

      while(curr):
        curr.prev = prev
        prev = curr
        curr = curr.next

      tail = prev

      while(n):
        tail = tail.prev
        n -= 1

      if not tail:
        return head.next

      tail.next = tail.next.next

      return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Optimal solution
# Fast and slow pointers
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      dummy = ListNode(0)
      dummy.next = head
      slow = dummy
      fast = dummy

      # move fast pointer n steps
      for _ in range(n):
        fast = fast.next
      
      # move slow pointer to prev node of deleting node
      while(fast.next):
        slow = slow.next
        fast = fast.next

      slow.next = slow.next.next

      return dummy.next
