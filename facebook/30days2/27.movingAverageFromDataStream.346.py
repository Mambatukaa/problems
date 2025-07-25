"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
 

Example 1:

Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
 

Constraints:

1 <= size <= 1000
-105 <= val <= 105
At most 104 calls will be made to next.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MovingAverage:
    def __init__(self, size):
        self.size = size

        self.head = Node(0)
        self.tail = self.head

        self.curr_sum = 0
        self.curr_size = 0


    def next(self, val):
        if self.curr_size == self.size:
            self.curr_sum -= self.head.next.val

            self.head = self.head.next
            self.curr_size -= 1
            # remove the oldest element
        

        newNode = Node(val)

        self.tail.next = newNode
        self.tail = self.tail.next

        self.curr_size += 1
        self.curr_sum += val


        return self.curr_sum / self.curr_size
        # return the average in the stream
        
from collections import deque

# queue
class MovingAverage:
    
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.curr_sum = 0


    def next(self, val):
        if len(self.queue) == self.size:
            self.curr_sum -= self.queue.popleft()
        
        self.queue.append(val)
        self.curr_sum += val

        return self.curr_sum / min(len(self.queue), self.size)
        # return the average in the stream
        
# array
# Time Complexity: O(M) M times next call
# Space Complexity: O(N)
class MovingAverage:
    
    def __init__(self, size):
        self.size = size
        self.array = [0] * size
        self.len = 0
        self.curr_sum = 0


    def next(self, val):
        index_to_replace = self.len % self.size

        if len(self.array) == self.size:
            self.curr_sum -= self.array[index_to_replace]
        
        self.array[index_to_replace] = val
        self.curr_sum += val
        self.len += 1

        return self.curr_sum / min(self.len, self.size)
        # return the average in the stream

movingAverage = MovingAverage(3)

print(movingAverage.next(1))
print(movingAverage.next(1))
print(movingAverage.next(1))
print(movingAverage.next(2))
print(movingAverage.next(2))
print(movingAverage.next(2))


""""

1. Initialize with the size 
2. Return the average of current array
3. If the size reaches the limit remove the first element from the array



Naive approach:

    size = 3

    1 -> 2 -> 3 -> 4 -> 5

    [1] --> sum(array) / min(self.size, len(array))

    --> 1

    [1, 2] -->

# Time Complexity: O(n) 


    size = 3

    1 -> 2 -> 3 -> 4 -> 5

    self.head = Node(0)
    self.tail = self.head

    self.size = size

    self.curr_size = 0
    self.curr_sum = 0


    next(val):
        
        if self.currSize == self.size:
            remove the head.next

            self.curr_sum -= head.next.val
            curr_size -= 1
            head = head.next

        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.curr_sum += val
        self.curr_size += 1

        return val / curr_size 







"""
