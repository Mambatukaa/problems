class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None



# Time Complexity: O(n)
# Space Complexity: O(n)
# RECURSIVE
def reverseII(head):
  def rec(prev, head):
    if not head:
      return prev

    dummy = head.next
    head.next = prev
    prev = head

    return rec(prev, dummy)

  return rec(None, head)

# Time Complexity: O(n)
# Space Complexity: O(1)
# Iterative
def reverse(head):
  dummy = None

  while head:
    headNext = head.next
    head.next = dummy
    dummy = head
    head = headNext

  return dummy


# 1 -> 2 -> 3 -> 4 -> 5
# 5 -> 4 -> 3 -> 2 -> 1
# newHead = 5


head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

temp = head

print("Before reverse")
while temp:
  print(temp.val)
  temp = temp.next

temp = reverseII(head)

print("******************************************************************************")

print("After reverse")
while temp:
  print(temp.val)
  temp = temp.next


