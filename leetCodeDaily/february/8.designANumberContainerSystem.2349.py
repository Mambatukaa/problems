""""

Design a number container system that can do the following:
• Insert or Replace a number at the given index in the system.
• Return the smallest index for the given number in the system.
Implement the NumberContainers class:
• NumberContainers () Initializes the number container system.
• void change(int index, int number) Fills the container at index with the number. If there is already a
number at that index, replace it.
• int find (int number) Returns the smallest index for the given number, or -1 if there is no index that is
filled by number in the system.

Example 1:
    Input:
    ["NumberContainers", "find", "change", "change", "change", "change", "find",
    "change", "find"]
    [[], [10], [2, 10], [1, 101, [3, 101, [5, 10], [10], [1, 20], [10]]

    Output:
    [null, -1, null, null, null, null, 1, null, 21



Constraints:
• 1 < index, number <= 109
• At most 105 calls will be made in total to change and find.

"""



from collections import defaultdict
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Sorted Set
class NumberContainers:
    def __init__(self):
        self.indexMap = {}
        self.numbersMap = defaultdict(SortedSet)
        
    def change(self, index: int, number: int) -> None:
        if index in self.indexMap:
            prev = self.indexMap[index]
            self.numbersMap[prev].remove(index)

            if not self.numbersMap[prev]:
                del self.numbersMap[prev]

        self.indexMap[index] = number
        self.numbersMap[number].add(index)
        

    def find(self, number: int) -> int:
        if number not in self.numbersMap:
            return -1

        return min(self.numbersMap[number])
        
from heapq import heappush, heappop
class NumberContainersII:
    def __init__(self):
        self.indexMap = {}
        self.numbersMap = defaultdict(list)
        
    def change(self, index: int, number: int) -> None:
        self.indexMap[index] = number
        heappush(self.numbersMap[number], index)
        

    def find(self, number: int) -> int:
        # keep checking top element until find the valid index
        while self.numbersMap[number]:
            index = self.numbersMap[number][0]

            # valid index found return it
            if self.indexMap[index] == number:
                return index
            
            # otherwise remove stale index
            heappop(self.numbersMap[number])

        return -1
        

nc = NumberContainersII()

print("Find 1:", nc.find(10))
nc.change(1, 10)
nc.change(2, 10)

print("Find 2:", nc.find(10))
nc.change(1, 20)

print("Find 3:", nc.find(10))
print("Find 4:", nc.find(20))



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
