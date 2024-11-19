class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None


# Time Complexity: O(n)
# Space Complexity: O(1)
def reverse(head):
  def rec(prev, head):
    if not head:
      return prev

    temp = head.next
    head.next = prev
    prev = head

    return rec(prev, temp)

  return rec(None, head)


# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
def addTwoNumbersII(l1, l2):
  reversedL1 = reverse(l1)
  reversedL2 = reverse(l2)

  carry = 0
  res = ListNode(0)
  curr = res

  while reversedL1 or reversedL2 or carry:
    reversedL1 = reversedL1 or ListNode(0)
    reversedL2 = reversedL2 or ListNode(0)

    total = reversedL1.val + reversedL2.val + carry

    carry = total // 10

    curr.next = ListNode(total % 10)
    curr = curr.next

    reversedL1 = reversedL1.next
    reversedL2 = reversedL2.next

  return reverse(res.next)

l1 = ListNode(2)
l1Node2 = ListNode(4)
l1Node3 = ListNode(3)

l1.next = l1Node2
l1Node2.next = l1Node3

l2 = ListNode(5)
l2Node2 = ListNode(6)
l2Node3 = ListNode(4)

l2.next = l2Node2
l2Node2.next = l2Node3

l3 = addTwoNumbersII(l1, l2)

while l3:
  print(l3.val)
  l3 = l3.next


"""
Add two numbers II

It's kind of same as add two numbers I. 
  We can use the same solution but firstly we should reverse the lists and add then we will reverse the response that reversed response will be our final response.

"""
