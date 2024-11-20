class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None


# Time Complexity: O(n)
# Space Complexity: O(n)
def mergeTwoSortedLists(list1, list2):
  res = ListNode(0)
  curr = res
  
  while list1 and list2:
    if list1.val < list2.val:
      res.next = list1
      list1 = list1.next
    else:
      res.next = list2
      list2 = list2.next

    res = res.next

  if list1:
    res.next = list1
  elif list2:
    res.next = list2

  return curr.next



l1Head = ListNode(1)
l1Node2 = ListNode(2)
l1Node3 = ListNode(4)

l1Head.next = l1Node2
l1Node2.next = l1Node3

l2Head = ListNode(1)
l2Node2 = ListNode(3)
l2Node3 = ListNode(4)

l2Head.next = l2Node2
l2Node2.next = l2Node3

l3 = mergeTwoSortedLists(l1Head, l2Head)

while l3:
  print(l3.val)
  l3 = l3.next
