# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return

        dic = {None: None}

        curr = head

        while curr:
            newNode = Node(curr.val)

            dic[curr] = newNode

            curr = curr.next

        curr = head

        while curr:
            node = dic[curr]
            node.next = dic[curr.next]
            node.random = dic[curr.random]
            curr = curr.next

        return dic[head]

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return


        curr = head

        while curr:
            next = curr.next
            curr.next = Node(curr.val)
            curr.next.random = curr.random
            curr.next.next = next

            curr = next

        curr = head.next

        while curr:
            next = curr.next
            curr.next = next.next if next else None
            curr.random = curr.random.next if curr.random else None

            curr = curr.next


        return head.next

