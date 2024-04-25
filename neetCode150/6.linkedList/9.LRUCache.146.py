class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity

        self.dic = {}

        # declaration of LL
        self.head = ListNode(9999, 99999)
        self.tail = ListNode(9999, 99999)

        self.head.next = self.tail
        self.tail.prev = self.head

    
    def shift(self, key):
        # update current location's connection
        currNode = self.dic[key]

        currNode.prev.next = currNode.next
        currNode.next.prev = currNode.prev

        # connect to the end
        currNode.prev = self.tail.prev
        currNode.next = self.tail

        self.tail.prev.next = currNode
        self.tail.prev = currNode
    
    def removeOld(self):
      del self.dic[self.head.next.key]
      self.head.next = self.head.next.next
      self.head.next.prev = self.head

    def get(self, key: int) -> int:
        # if key not exists
        if key not in self.dic:
            return -1

        # shift node to the end
        self.shift(key)

        # return value
        return self.dic[key].value
        

    def put(self, key: int, value: int) -> None:
      # if node exists
      if key in self.dic:
        # update value
        node = self.dic[key]
        node.value = value

        self.shift(key)
        return

      # if size reaches the limit
      if self.size == self.capacity:
        # remove old element
        self.removeOld()
        self.size -= 1

      # if node didn't exist
      # add new node to the end
      newNode = ListNode(key, value)

      newNode.prev = self.tail.prev
      newNode.next = self.tail

      self.tail.prev.next = newNode
      self.tail.prev = newNode

      self.dic[key] = newNode
      self.size += 1


