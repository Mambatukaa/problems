

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
