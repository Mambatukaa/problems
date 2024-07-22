from heapq import heappop, heappush

class ListNode:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

# Simple Naive solution
# BRUTE FORCE
# Time Complexity: O(n log n)
# Space Complexity: O(n) n - total nodes
def mergeKLists(lists):
  head = point = ListNode(0)

  nodes = []

  for l in lists:
    while l:
      nodes.append(l.val)
      l = l.next

  for node in sorted(nodes):
    point.next = ListNode(node)
    point = point.next

  return head.next


# COMPARE ONE BY ONE
# Time Complexity: O(nk)
# Space Complexity: O(n) n - total nodes


# minHeap

class HeapNode:
  def __init__(self, node):
    self.node = node

  def __lt__(self, other):
    # Define comparison based on ListNode's value
    return self.node.val < other.node.val

# Min heap OPTIMIZED Sort Solution
# Time Complexity: O(n log k)
# Space Complexity: O(n)
def mergeKListsII(lists):
  heap = []

  dummy = ListNode(0)
  curr = dummy

  for l in lists:
    if l:
      heappush(heap, HeapNode(l))

  while heap:
    l = heappop(heap)
    node = l.node

    curr.next = node
    curr = curr.next

    if node.next:
      heappush(heap, HeapNode(node.next))

  return dummy.next

# Time Complexity: O(n * log k) where k is the number of linked lists.
# Space Complexity: O(1)
def mergeKListsIII(lists):
  n = len(lists)

  if not n:
    return

  # Merge two lists
  def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
      if l1.val > l2.val:
        curr.next = l2
        l2 = l2.next
      else:
        curr.next = l1
        l1 = l1.next
      curr = curr.next

    curr.next = l1 if l1 else l2

    return dummy.next
  
  for i in range(n):
    if i + 1 < n:
      lists[i + 1] = mergeTwoLists(lists[i], lists[i + 1])

  return lists[n - 1]



# NOTE First List
fNode3 = ListNode(5)
fNode2 = ListNode(4, fNode3)
fNode1 = ListNode(1, fNode2)

# NOTE Second List
sNode3 = ListNode(4)
sNode2 = ListNode(3, sNode3)
sNode1 = ListNode(1, sNode2)

# NOTE Third List
tNode2 = ListNode(6)
tNode1 = ListNode(2, tNode2)

lists = [fNode1, sNode1, tNode1]

mergedNode = mergeKListsIII(lists)

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



