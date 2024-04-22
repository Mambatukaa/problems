# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity: O(n)
# Space Complexity: O(1)
# 8 minutes
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      prev = None

      while(head):
        dummy = head.next
        head.next = prev
        
        prev = head
        head = dummy
      
      return prev


        







"""

1 -> 2 -> 3 -> 4 -> 5

Reverse Linked list

Reverse it iteratively and recursively



head = 1 -> 2 -> 3 -> 4 -> 5

                            p         
                            h   d   
prev <- 1 <- 2 <- 3 <- 4 <- 5


dummy = head.next
head.next = prev;

prev = head;
head = dummy;


while(head):



return prev;








"""
