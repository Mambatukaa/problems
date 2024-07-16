class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

# Time Complexity: O(n)
# Space Complexity: O(1)
def mergeTwoSortedList(l1, l2):
  dummy = ListNode(0)
  curr = dummy

  while l1 and l2:
    # compare values

    if l1.val > l2.val:
      curr.next = l2
      l2 = l2.next
    else:
      curr.next = l1
      l1 = l1.next

    curr = curr.next

  if l1:
    curr.next = l1
  elif l2:
    curr.next = l2

  return dummy.next

# Time Complexity: O(n)
# Space Complexity: O(n)
def mergeTwoSortedListII(l1, l2):
  if not l1:
    return l2
  elif not l2:
    return l1
  elif not l1 and not l2:
    return None
  elif l1.val < l2.val:
    l1.next = self.mergeTwoLists(l1.next, l2)
    return l1
  else:
    l2.next = self.mergeTwoLists(l1, l2.next)
    return l2

"""

l1 = 1 2 4
l2 = 1 3 4


merged = 1 1 2 3 4 4


declare dummy node

start to compare 

"""
