""""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding
window.
Implement the MovingAverage class:
• MovingAverage (int size) Initializes the object with the size of the window size.
• double next(int val) Returns the moving average of the last size values of the stream.

Example 1:
Input
    ["MovingAverage", "next", "next", "next", "next"]
    [[3], [1], [10], [3], [5]]
Output

    [null, 1.0, 5.5, 4.66667, 6.0]

Explanation
    MovingAverage movingAverage = new MovingAverage (3) ;
    movingAverage.next(1); // return 1.0 = 1 / 1
    movingAverage.next (10); // return 5.5 = (1 + 10) / 2
    movingAverage.next (3); // return 4.66667 = (1 + 10 + 3) / 3
    movingAverage.next (5): // return 6.0 = (10 + 3+5) / 3



Constraints:
• 1 <= size <= 1000
• -10^5 <= val <= 10^5
• At most 104 calls will be made to next.

"""

from collections import deque
# Time Complexity: O(1)
# Space Complexity: O(n)
# deque
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.currSum = 0

    def next(self, val: int) -> float:
        if self.size == len(self.queue):
            self.currSum -= self.queue.popleft()

        self.currSum += val
        self.queue.append(val)

        return self.currSum / len(self.queue)
        
# Time Complexity: O(1)
# Space Complexity: O(n)
# Circular queue
class MovingAverage1:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * size
        self.window_sum = self.head = 0

        # count of current elements
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1

        tail = (self.head + 1) % self.size

        self.window_sum = self.window_sum - self.queue[tail] + val

        # new head index
        self.head = tail
        self.queue[self.head] = val

        return self.window_sum / min(self.size, self.count)

movingAverage = MovingAverage(3);
print(movingAverage.next(1)) # // return 1.0 = 1 / 1
print(movingAverage.next(10)) # // return 5.5 = (1 + 10) / 2
print(movingAverage.next(3))  #// return 4.66667 = (1 + 10 + 3) / 3
print(movingAverage.next(5))  #// return 6.0 = (10 + 3 + 5) / 3

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
