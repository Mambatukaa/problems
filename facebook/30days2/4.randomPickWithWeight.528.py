import random 
class Solution:


    # Time Complexity: O(w)
    # Space Complexity: O(n)
    def __init__(self, w):
        self.prefix_sum = []

        prefix = 0

        for weight in w:
            prefix += weight
            self.prefix_sum.append(prefix)

        self.total_sum = prefix

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def pickIndex(self) -> int:
        target = self.total_sum * random.random()

        for i, prefix_sum in enumerate(self.prefix_sum):
            if target < prefix_sum:
                return i

    def pickIndexBinarySearch(self) -> int:
        target = self.total_sum * random.random()

        l = 0
        r = len(self.prefix_sum)

        while l < r:
            midIdx = l + (r - l) // 2

            if target > self.prefix_sum[midIdx]:
                l = midIdx + 1
            else:
                r = midIdx
        return l



"""

1. Calculate the prefix
2. random offset target
3. linear search


"""



w = [1]
solution = Solution(w)

print(solution.pickIndexBinarySearch())
        

        



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()



"""
     0
w = [1]

i =  0  1
w = [1, 3] ---> [0, 1, 1, 1]
w = [1, 3, 5] ---> [0, 1, 1, 1, 5, 5, 5, 5, 5]

1 / 9 = 0.1
3 / 9 = 0.3
5 / 9 = 0.5

probability = w[i] / sum(w)



"""
