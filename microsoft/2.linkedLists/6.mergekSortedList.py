class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

# Time Complexity: O(k)
# Space Complexity: O(k)
def mergeTwoLists(l1, l2):
  dummy = ListNode(0)
  res = dummy

  while l1 and l2:
    if l1.val < l2.val:
      dummy.next = l1
      l1 = l1.next
    else:
      dummy.next = l2
      l2 = l2.next

    dummy = dummy.next

  print(l1, l2)
  if not l1:
    dummy.next = l2
  if not l2:
    dummy.next = l1

  return res.next

# Time Complexity: O(n * k)
# Space Complexity: O(k)
def mergeKSortedLists(lists):
  n = len(lists)

  if not n:
    return None
  if n == 1:
    return lists[0]

  for i in range(n - 1):
    # merge i and i + 1 to lists[i + 1]
    lists[i + 1] = mergeTwoLists(lists[i], lists[i + 1])

  return lists[n - 1]

# NEETCode approach 
# Time Complexity: O(log k * n)
# Space Complexity: O(k)
def mergeKSortedListsII(lists):
  if not len(lists):
    return None

  while len(lists) > 1:
    mergedLists = []

    for i in range(0, len(lists), 2):
      l1 = lists[i]
      l2 = lists[i + 1] if i + 1 < len(lists) else None

      mergedLists.append(mergeTwoLists(l1, l2))

    lists = mergedLists

  return lists[0]

# 1st list
l1 = ListNode(1)
l1Node2 = ListNode(4)
l1Node3 = ListNode(5)

l1.next = l1Node2
l1Node2.next = l1Node3

# 2nd list
l2 = ListNode(1)
l2Node2 = ListNode(3)
l2Node3 = ListNode(4)

l2.next = l2Node2
l2Node2.next = l2Node3

# 3rd list
l3 = ListNode(2)
l3Node2 = ListNode(6)
l3.next = l3Node2

lists = [l1, l2]

res = mergeKSortedListsII(lists)

while res:
  print(res.val)
  res = res.next

"""

Merge K sorted lists


You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
