class ListNode:

  def __init__(self, key, val):
    self.val = val
    self.next = None
    self.prev = None
    self.key = key


class LRUCache:
  def __init__(self, capacity):
    self.capacity = capacity
    self.size = 0

    self.head = ListNode(0, 0)
    self.tail = ListNode(0, 0)

    self.head.next = self.tail
    self.tail.prev = self.head
    
    self.cache = {}

    print("Successfully created cache with capacity:", capacity)

  # Time Complexity: O(1)
  def put(self, key, value):

    # if key exists in cache remove the key
    if key in self.cache:
      node = self.cache[key]

      node.next.prev = node.prev
      node.prev.next = node.next

      del self.cache[key]

      self.size -= 1

    # if size reaches the limit
    if self.size == self.capacity:
      # remove the least recently used key
      oldNode = self.tail.prev

      oldNode.prev.next = self.tail
      self.tail.prev = oldNode.prev

      del self.cache[oldNode.key]
      
      self.size -= 1

    # if key doesn't exists add to the head
    # create new node
    newNode = ListNode(key, value)
    headNext = self.head.next

    self.head.next = newNode
    headNext.prev = newNode
    newNode.next = headNext
    newNode.prev = self.head

    self.cache[key] = newNode
    self.size += 1

  # Time Complexity: O(1)
  def get(self, key):
    if key in self.cache:
      node = self.cache[key]

      # remove node from current position
      node.prev.next = node.next
      node.next.prev = node.prev
      
      # move node to the head
      self.head.next.prev = node
      node.next = self.head.next

      self.head.next = node
      node.prev = self.head

      return self.cache[key].val
    
    return -1

lruCache = LRUCache(1)

lruCache.put(2, 1)
print("get:", lruCache.get(2))
lruCache.put(2, 2)

print("get:", lruCache.get(2))


print(lruCache.cache)

"""
If the number of keys exceeds the capacity from this operation, evict the least recently used key.




If size reaches the limit. Remove the recent used key.


put(1, 1)

{1: 1}

put(2, 2)

{
  1: 1,
  2: 2
}

put(3, 3)

{
  1: 1,
  2: 2,
  3: 3
}


get(1)

{
  2: 2,
  3: 3,
  1: 1
}



1 <-> 2 <-> 3

get(2)


2 <-> 1 <-> 3

put(4) 

4 <-> 2 <-> 1



add the key and value to the head. 

move the key to the head when get method calledc


cache = {

  key: Node(value)


}

"""
