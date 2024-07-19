class ListNode:
  def __init__(self, val, next = None, random = None):
    self.val = val
    self.next = next
    self.random = random


head = ListNode(7)

node2 = ListNode(13)
node3 = ListNode(11)
node4 = ListNode(10)
node5 = ListNode(1)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


node2.random = head
node3.random = node5
node4.random = node3
node5.random = head

# Time Complexity: O(n)
# Space Complexity: O(n)
# 2 passes solution
# Iteration
def deepCopy(head):
  dic = {None: None}

  curr = head

  while curr:
    copy = ListNode(curr.val)
    dic[curr] = copy

    curr = curr.next

  curr = head

  while curr:
    copy = dic[curr]
    copy.next = dic[curr.next]
    copy.random = dic[curr.random]

    curr = curr.next

  return dic[head]

# Recursive
# Time Complexity: O(n)
# Space Complexity: O(n)
def deepCopyII(head):
  oldToCopy = {}

  def helper(head):
    if not head:
      return None

    if head in oldToCopy:
      return oldToCopy[head]

    node = ListNode(head.val)
    oldToCopy[head] = node

    node.next = helper(head.next)
    node.random = helper(head.random)

    return node

  return helper(head)

# Single pass
# Time Complexity: O(n)
# Space Complexity: O(1)
def deepCopyIII(head):
  if not head:
    return None

  curr = head

  while curr:
    newNode = ListNode(curr.val)

    newNode.next = curr.next
    curr.next = newNode
    curr = newNode.next

  curr = head

  while curr:
    curr.next.random = curr.random.next if curr.random else None
    curr = curr.next.next

  newHead = head.next
  curr = newHead

  while curr and curr.next:
    curr.next = curr.next.next
    curr = curr.next

  return newHead

copyHead = deepCopyIII(head)

print("***************************")

while copyHead:
  print(copyHead.val)
  if copyHead.random:
    print("ran:", copyHead.random.val)
  copyHead = copyHead.next
