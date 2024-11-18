class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None


# Time Complexity: O(n)
# Space Complexity: O(1)
# Fast and Slow 
def hasCycle(head):
  if not head:
    return False
  
  slow = head
  fast = head.next

  while fast and fast.next:
    if slow == fast:
      return True

    slow = slow.next
    fast = fast.next.next


  return False

head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2


print("res:", hasCycle(head))


"""

naive solution: Collect numbers in the list and check duplication


Fast and slow pointers



"""
