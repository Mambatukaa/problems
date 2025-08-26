"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?







"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevLeft, curr = dummy, head

        # 1. Reach node at position left
        for _ in range(left - 1):
            prevLeft = curr
            curr = curr.next
        
        prev = None
        # 2. Reverse from left to right
        for i in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Update the pointers
        prevLeft.next.next = curr
        prevLeft.next = prev

        return dummy.next
        

        


"""


1. Reach the node to the left node
    a. Save the left previous node later left previous node will point to right node
    b. left node will point to the right next node
2. Reverse the node until reaches the right node

3. 


     p
     ^
     |    p
1 -> 2 <- 3 <- 4 -> 5
pl             c


l = 2
r = 4

1 -> 2 -> 3 -> 4 -> 5

1 -> 4 -> 3 -> 2 -> 5



l = 1
r = 4


                       p
None <- 1 <- 2 -> 3 <- 4 -> 5
pl                          c

4 -> 3 -> 2 -> 1 -> 5


"""
