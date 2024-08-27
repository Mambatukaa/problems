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

  def removeOld(self):
    # remove old node from tail
    node = self.tail.prev

    node.prev.next = self.tail
    self.tail.prev = node.prev

    del self.cache[node.key]

  def shiftToHead(self, node):
    # remove node from current location
    node.prev.next = node.next
    node.next.prev = node.prev

    # add new connections to current node
    node.prev = self.head
    node.next = self.head.next

    # update tail
    node.next.prev = node
    self.head.next = node

  # Time Complexity: O(1)
  def put(self, key, value):
    # if key exists in cache update the value and shift to tail
    if key in self.cache:
      node = self.cache[key]
      node.val = value

      self.shiftToHead(node)

      return

    # if size reaches the limit
    if self.size == self.capacity:
      self.removeOld()
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

      self.shiftToHead(node)

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
