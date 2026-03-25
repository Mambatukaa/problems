""""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""


class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val

        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.dic = {}
        self.capacity = capacity
        self.size = 0
        

    def get(self, key: int) -> int:
        # if exists return and move to the tail
        if key not in self.dic:
            return -1

        val = self.dic[key].val

        self.delete(key)
        self.put(key, val)
        
        return self.dic[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.delete(key)

        node = ListNode(key, value)
        
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node

        self.size += 1
        self.dic[key] = node

        if self.size > self.capacity:
            # remove the old node
            self.delete(self.head.next.key)

    def delete(self, key: int) -> None:
        node = self.dic[key]
        nxt = node.next

        node.prev.next = nxt
        nxt.prev = node.prev


        self.size -= 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


"""
{
    1: 1, 2: 2, 3: 3
}


head -> 1 -> 2 -> 3 -> tail


get(1)

2 -> 3 -> 1




"""


class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val

        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.dic = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        node = self.dic[key]

        self.remove(node)
        self.add(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)

        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]

    def add(self, node):
        prev_end = self.tail.prev
        prev_end.next = node

        node.prev = prev_end
        node.next = self.tail

        self.tail.prev = node

    def remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


"""
{
    1: 1, 2: 2, 3: 3
}


head -> 1 -> 2 -> 3 -> tail


get(1)

2 -> 3 -> 1




"""