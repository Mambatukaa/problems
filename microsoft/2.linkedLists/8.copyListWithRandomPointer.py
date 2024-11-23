from collections import defaultdict

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.random = None


# Hash MAP
# Time Complexity: O(n)
# Space Complexity: O(n)
def copyRandomList(head):
  if not head:
    return None

  # Add each nodes to hashmap with a copy node
  copy = defaultdict(ListNode)

  curr = head 

  while curr:
    copy[curr] = ListNode(curr.val)
    curr = curr.next

  # iterate through nodes and update pointer
  newHead = copy[head]
  curr = newHead

  while head:
    curr.next = copy[head.next] if head.next else None
    curr.random = copy[head.random] if head.random else None

    curr = curr.next
    head = head.next


  return newHead


head = ListNode(7)

node2 = ListNode(13)
node3 = ListNode(11)
node4 = ListNode(10)
node5 = ListNode(1)

head.next = node2

node2.next = node3
node2.random = head

node3.next = node4
node3.random = node5

node4.next = node5
node4.random = node3

node5.random = head


res = copyRandomList(head)

while res:
  print(res.val, res.random.val if res.random else "-----")
  res = res.next
