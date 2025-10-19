""""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?



Naive solution

1. Append num to the array
2. Sort the array and return median

Time Complexity: O(n log n) on every operation 
Space Complexity: O(n) res array



2 --> 1 --> 3 --> 4 --> 5 --> 6

Two heaps solution (Store one more or equal elements than bigger_elements_heap in smaller_elements_heap 

1. Max heap for smaller elements
2. Min heap for bigger elements

3. If the size of the heaps are equal get the values from heaps and return the average 
4. Else get the element from smaller_heap and return it

5. when add  

smaller_heap = [] max_heap # the elements are must be less than or equal to the bigger_heap elements
bigger_heap = [] min_heap #


2 --->  
        if not smaller_heap and not bigger_heap:

            add to the smaller heap

            smaller_heap = [2]
            bigger_heap = []


1 ----->
        
        if smaller_heap[0] > value:
            heappush(bigger_heap, heappop(smaller_heap))
            heappush(smaller_heap, value)

            smaller_heap = [1]
            bigger_heap = [2]


3 ---> 
    
        if smaller_heap[0] < value:
            heappush(bigger_heap, value)

            smaller_heap = [1]
            bigger_heap = [2, 3]

            if len(bigger_heap) > len(smaller_heap):
                
                heappush(smaller_heap, heappop(bigger_heap)

                smaller_heap = [2, 1]
                bigger_heap = [3]



4 ---->

    







        
    
    


"""



from heapq import heappush, heappop
# 20 minutes
# Time Complexity: O( log n)
class MedianFinder:
    def __init__(self):
        self.smaller_heap = [] # max_heap
        self.bigger_heap = [] # min_heap


    def addNum(self, num: int) -> None:
        if not len(self.smaller_heap) and not len(self.bigger_heap):
            heappush(self.smaller_heap, -num)
            return

        # add num to the smaller_heap and adjust
        if -self.smaller_heap[0] > num:
            heappush(self.smaller_heap, -num)

            # if smaller_heap has two more elements than bigger_heap. add the first element to the bigger_heap
            if len(self.smaller_heap) > len(self.bigger_heap) + 1:
                heappush(self.bigger_heap, -heappop(self.smaller_heap))

        else:
            heappush(self.bigger_heap, num)

            if len(self.smaller_heap) < len(self.bigger_heap):
                heappush(self.smaller_heap, -heappop(self.bigger_heap))

        

    def findMedian(self) -> float:
        if self.bigger_heap and len(self.smaller_heap) ==  len(self.bigger_heap):
            # return the average of first elements of two heaps

            return (-self.smaller_heap[0] + self.bigger_heap[0]) / 2
        
        return -self.smaller_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
#

class MedianFinder:
    def __init__(self):
        self.count = [0] * 101  # Since numbers are in range 0 to 100
        self.total = 0

    def addNum(self, num: int) -> None:
        self.count[num] += 1
        self.total += 1

        print(self.count)

    def findMedian(self) -> float:
        mid1 = self.total // 2
        mid2 = mid1 + 1
        count_sum = 0
        first = None
        second = None

        for i in range(101):
            count_sum += self.count[i]
            if first is None and count_sum >= mid1 + 1:
                first = i
            if count_sum >= mid2:
                second = i
                break

        if self.total % 2 == 1:
            return second
        else:
            return (first + second) / 2


import heapq

class MedianFinder:
    def __init__(self):
        self.count = [0] * 101
        self.total_in_range = 0
        self.low = []   # max heap for numbers < 0
        self.high = []  # min heap for numbers > 100
        self.total = 0

    def addNum(self, num: int) -> None:
        if 0 <= num <= 100:
            self.count[num] += 1
            self.total_in_range += 1
        elif num < 0:
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.high, num)
        self.total += 1

    def findMedian(self) -> float:
        mid1 = self.total // 2
        mid2 = mid1 + 1
        is_even = self.total % 2 == 0

        # Convert counts + heaps to sorted stream simulation
        merged = []

        # Pull from maxHeap (low), in reverse order
        low_sorted = sorted([-x for x in self.low])
        merged.extend(low_sorted)

        # Pull from count array
        for num in range(101):
            merged.extend([num] * self.count[num])

        # Pull from minHeap (high)
        high_sorted = sorted(self.high)
        merged.extend(high_sorted)

        if is_even:
            return (merged[mid1 - 1] + merged[mid2 - 1]) / 2
        else:
            return merged[mid1]

obj = MedianFinder()

obj.addNum(-1)
print(obj.findMedian())
obj.addNum(1)
print(obj.findMedian())
obj.addNum(101)
print(obj.findMedian())

""""


0 1 2 3 4 5 6 7 8
0 1 2 1 1 1 1 1 1

1, 2, 2, 3, 4, 5, 6, 7, 8 
    total = 9
    mid1 = 4
    mid2 = 5



reach the first 4th element and 5th element

4th element = 3
5th element = 4

if total % 2 == 1:
    return second
return first + second / 2





"""

