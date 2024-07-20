class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

# Time Complexity: O(n * k)
# Space Complexity: O(1)
def reverseNodes(head, k):
  def getKthNode(curr, k):
    while curr and k > 0:
      curr = curr.next
      k -= 1
    return curr

  dummy = ListNode(0, head)
  groupPrev = dummy

  while True:
    kth = getKthNode(groupPrev, k)

    if not kth:
      break

    groupNext = kth.next

    # reverse Group
    prev, curr = kth.next, groupPrev.next

    while curr != groupNext:
      tmp = curr.next
      curr.next = prev
      prev = curr
      curr = tmp

    # save groupPrev.next that is first element of group
    temp = groupPrev.next
    # kth element will connect to the last group's tail
    groupPrev.next = kth
    # the last group's first element will be next group's previous element
    groupPrev = temp

  return dummy.next 

head = ListNode(1)

node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

k = 2

head = reverseNodes(head, k)


print("****************************************************************************************************************")
curr = head

while curr:
  print(curr.val)
  curr = curr.next
