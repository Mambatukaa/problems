
""""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)





"""

"""

Complexity Analysis

Time Complexity: O( 
K
N
​
 ) where N is the number of all possible values and K is the number of predefined buckets, which is 769.

Assuming that the values are evenly distributed, thus we could consider that the average size of bucket is  
K
N
​
 .

Since for each operation, in the worst case, we would need to scan the entire bucket, hence the time complexity is O( 
K
N
​
 ).


Space Complexity: O(K+M) where K is the number of predefined buckets, and M is the number of unique values that have been inserted into the HashSet.


"""

class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class Bucket:
    def __init__(self):
        self.head = Node(0)

    def insert(self, newValue):
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            self.head.next = newNode


    def delete(self, value):
        prev = self.head
        curr = self.head.next

        while curr:
            if curr.value == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next

        while curr:
            if curr.value == value:
                return True
            curr = curr.next

        return False


class MyHashSet:

    def __init__(self):
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]
    
    def _hash(self, key):
        return key % self.keyRange

    def add(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key: int) -> None:
        bucketIndex = self._hash(key)

        self.bucketArray[bucketIndex].delete(key)
        

    def contains(self, key: int) -> bool:
        bucketIndex = self._hash(key)

        return self.bucketArray[bucketIndex].exists(key)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)