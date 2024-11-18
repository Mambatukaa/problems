class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None

# Time Complexity: O(n)
# Space Complexity: O(1)
def addTwoNumbers(l1, l2):
  res = ListNode(0)
  dummy = res
  carry = 0


  while l1 or l2 or carry:
    l1 = l1 or ListNode(0)
    l2 = l2 or ListNode(0)

    add = l1.val + l2.val + carry

    carry = add // 10

    res.next = ListNode(add % 10)
    res = res.next

    l1 = l1.next
    l2 = l2.next

  return dummy.next


l1Head = ListNode(0)

l2Head = ListNode(0)


l3Head = addTwoNumbers(l1Head, l2Head)

while l3Head:
  print(l3Head.val)
  l3Head = l3Head.next

"""
Ex 1:
  l1 = 2 -> 4 -> 3
  l2 = 5 -> 6 -> 4

  l3 = 7 -> 0 -> 8

Ex 2:
  l1 = 9 -> 9 -> 9
  l2 = 9 -> 9

  l3 = 8 -> 9 -> 0 -> 1

""" 
