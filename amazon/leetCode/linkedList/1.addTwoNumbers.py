
class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next


# Time Complexity: O(max(n, m))
# Space Complexity: O(1)
def addTwoNumbers(l1, l2):
  dummy = ListNode()
  curr = dummy

  carry = 0
  while l1 or l2 or carry:
    v1 = l1.val if l1 else 0
    v2 = l2.val if l2 else 0

    val = v1 + v2 + carry

    carry = val // 10

    # new digit
    val = val % 10
    curr.next = ListNode(val)

    # update pointers
    curr = curr.next
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None

  return dummy.next

l1 = ListNode(9)
node2 = ListNode(9)
node3 = ListNode(9)

l1.next = node2
node2.next = node3


l2 = ListNode(9)
node5 = ListNode(9)

l2.next = node5

newNode = addTwoNumbers(l1, l2)

print("========================================")
while newNode:
  print(newNode.val)
  newNode = newNode.next


"""
l1 = 9999999
l2 = 9999
     
   = 89990001



1. Use two pointers and starts to add nums.
2. If there is additional num save it


"""
