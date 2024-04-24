# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity: O(n + m)
# Space Complexity: O(1)
# Gave up 
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      dummy = ListNode()
      cur = dummy
      carry = 0

      while(l1 or l2 or carry):
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        newDigit = v1 + v2 + carry
        remainder = newDigit % 10

        carry = newDigit // 10

        cur.next = ListNode(remainder)
        cur = cur.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

      return dummy.next



        










        




"""

v1 + v2 + carry

calculate new v1 and v2 and carry


"""
