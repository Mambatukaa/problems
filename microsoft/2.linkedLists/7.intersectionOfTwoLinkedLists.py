class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None


# COUNT THE TOTAL NODES
# START WITH SAME DESTINATION
def intersectionOfTwoLinkedLists(headA, headB):
  l1, l2 = headA, headB

  while l1 != l2:
    l1 = l1.next if l1 else headB
    l2 = l2.next if l2 else headA

  return l1


listA = ListNode("a1")
listANode2 = ListNode("a2")

listA.next = listANode2


listB = ListNode("b1")
listBNode2 = ListNode("b2")
listBNode3 = ListNode("b3")

listB.next = listBNode2
listBNode2.next = listBNode3


listC = ListNode("c1")
listCNode2 = ListNode("c2")
listCNode3 = ListNode("c3")
listC.next = listCNode2
listCNode2.next = listCNode3

listANode2.next = listC
listBNode3.next = listC

res = intersectionOfTwoLinkedLists(listA, listB)

while res:
  print(res.val)
  res = res.next

"""

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.


A:       a1 -> a2
                  \
                   c1 -> c2 -> c3
                  /
B: b1 -> b2 -> b3

Output: c1




Custom Judge:
  The inputs to the judge are given as follows (your program is not given these inputs):
    • intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected
    node.
    • listA - The first linked list.
    • listB - The second linked list.
    • SkipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
    • skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
  The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to
  your program. If you correctly return the intersected node, then your solution will be accepted.


"""
