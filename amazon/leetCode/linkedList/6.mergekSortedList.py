class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

# Simple Naive solution
# Time Complexity: O(n)
# Space Complexity: O(n) n - total nodes
def mergeKLists(lists):

  nodes = []

  for lList in lists:
    curr = lList

    while curr:
      nodes.append(curr)
      curr = curr.next

  def sortByVal(node):
    return node.val

  nodes.sort(key=sortByVal)

  dummy = Node(0)
  curr = dummy

  for node in nodes:
    curr.next = node
    curr = curr.next

  return dummy.next





# NOTE First List
fNode3 = Node(5)
fNode2 = Node(4, fNode3)
fNode1 = Node(1, fNode2)

# NOTE Second List
sNode3 = Node(4)
sNode2 = Node(3, sNode3)
sNode1 = Node(1, sNode2)

# NOTE Third List
tNode2 = Node(6)
tNode1 = Node(2, tNode2)

lists = [fNode1, sNode1, tNode1]

mergedNode = mergeKLists(lists)

while mergedNode:
  print("val:", mergedNode.val)
  mergedNode = mergedNode.next


"""
Given an array of k linked-lists lists, each linked list is sorted in ascending order.
Merge all linked lists into one sorted linked list and return it.


Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]


Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]

merging them into one sorted list:
1->1->2->3->4->4->5->6


1 -> 4 -> 5
1 -> 3 -> 4
2 -> 6

"""



