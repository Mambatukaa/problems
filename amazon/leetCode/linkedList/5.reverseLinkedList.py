class ListNode:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

# Time Complexity: O(n)
# Space Complexity: O(1)
def reverseLL(head):
  prev = None
  curr = head


  while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp

  return prev

# Time Complexity: O(n)
# Space Complexity: O(n)
def reverseLLII(head):
  def helper(prev, curr):
    if not curr:
      return prev

    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp

    return helper(prev, curr)
    
  return helper(None, head)

# Time Complexity: O(n)
# Space Complexity: O(n)
def reverseLLIII(head):
  if not head or not head.next:
    return head

  p = reverseLLIII(head.next)

  head.next.next = head
  head.next = None

  return p



head = ListNode(1)

node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = reverseLLIII(head)

while head:
  print(head.val)
  head = head.next



