"""


A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in
the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its
value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to
new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the
pointers in the new list should point to nodes in the original list.
For example, if there are two nodes X and Y in the original list, where X. random -> Y, then for the corresponding two nodes
x and y in the copied list, x. random —> y .
Return the head of the copied linked list.
The linked list is represented in the input/output as a list of in nodes. Each node is represented as a pair of [val,
random_index] where:
    • val: an integer representing Node.val
    • random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point
    to any node.
    Your code will only be given the head of the original linked list.


Ex 1:

Input: head = [[7,null],[13,0],[11,4],[10,21,[1,01]
Output: [[7,null], [13,0], [11,4], [10,21, [1,0]]

"""


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
        nodesMap = {None: None}

        curr = head

        while curr:
            nodesMap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            copy = nodesMap[curr]

            copy.random = nodesMap[curr.random]
            copy.next = nodesMap[curr.next]
            curr = curr.next

        return nodesMap[head]

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def copyRandomListII(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        curr = head

        while curr:
            newNode = Node(curr.val, curr.next)
            curr.next = newNode

            curr = curr.next.next

        curr = head

        while curr and curr.next:
            next = curr.next.next if curr.next else None

            curr.next.next = next.next if next else None
            curr.next.random = curr.random.next if curr.random else None

            curr = next

        return head.next

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Clean code but 3 iterations
    def copyRandomListIII(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        curr = head

        # next connection
        while curr:
            newNode = Node(curr.val, curr.next)
            curr.next = newNode

            curr = curr.next.next

        curr = head

        # random connection
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next

        # remove old list
        curr = head.next

        while curr:
            next = curr.next.next if curr.next else None

            curr.next = next
            curr = next

        return head.next


head = Node(7)

node2 = Node(13)
node3 = Node(11)

node4 = Node(10)
node5 = Node(1)

head.next = node2

node2.next = node3
node2.random = head

node3.next = node4
node3.random = node5

node4.next = node5
node4.random = node3

node5.random = head


solution = Solution()
print("res:", solution.copyRandomListIII(head))
