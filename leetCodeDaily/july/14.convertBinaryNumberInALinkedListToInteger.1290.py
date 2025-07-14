""""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
 

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.















"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:

        # find the length of the linked list
        # 101 
        # n = 3
        # res += el * index 

        n = 0

        curr = head

        while curr:
            n += 1
            curr = curr.next
        

        curr = head
        res = 0

        exponent = n - 1

        while curr:
            res += curr.val * (2 ** exponent)
            curr = curr.next
            exponent -= 1

        return res


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0

        while head:
            print(result << 1)
            result = (result << 1) | head.val

            head = head.next

        return result
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0

        while head:
            result = result * 2 + head.val
            head = head.next

        return result
        


"""
 4 3 2 1 0
[1,0,1,1,0]

0 * 2 + 1 = 1
1 * 2 + 0 = 2
2 * 2 + 1 = 5
5 * 2 + 1 = 11
11 * 2 + 0 = 22

"""
