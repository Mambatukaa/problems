"""
Complexity Analysis

Given n as the length of nums and m as maxValue - minValue,

Time complexity: O(n+m)

We first find maxValue and minValue, which costs O(n).

Next, we initialize count, which costs O(m).

Next, we populate count, which costs O(n).

Finally, we iterate over the indices of count, which costs up to O(m).

Space complexity: O(m)

We create an array count with size O(m).



"""

class Solution:
    # Time Complexity: O(n + m) where n is the length of nums and m is maxValue - minValue
    # Space Complexity: O(m)
    def findKthLargest(self, nums, k):
        minValue = min(nums)
        maxValue = max(nums)

        count = [0] * (maxValue - minValue + 1)

        print(count)

        for num in nums:
            count[num - minValue] += 1

        print(count)

        remaining = k

        for num in range(len(count) -1, -1, -1):
            remaining -= count[num]

            if remaining <= 0:
                return num + minValue

        return -1

import random
class Solution:
    

    # Time Complexity: O(n) on average, O(n^2) in the worst case
    # Space Complexity: O(n)
  # Quick Select Algorithm
  # Hoare's Partitioning
    def findKthLargest(self, nums, k):

        def quickSelect(nums, k):
            pivot = random.choice(nums)
            left = []
            mid = []
            right = []

            for num in nums:
                if num > pivot:
                    right.append(num)
                elif num < pivot:
                    left.append(num)
                else:
                    mid.append(num)

            if len(right) >= k:
                return quickSelect(right, k)

            if len(right) + len(mid) < k:
                return quickSelect(left, k - len(right) - len(mid))
            return pivot

        return quickSelect(nums, k)
                

            





"""
Quick select

choose random number -- pivot

iterate through nums and split the numbers

[3, 5, 8, 8, 8, 10] k = 6 ==> 6

pivot = 5

left = [3]
mid = [5]
right = [8, 8, 8, 10]


if len(right) >= k:
    # the answer must be in right
    quickSelect(right, k)

if len(mid) + len(right) < k:
    # the answer must be in left
    quickSelect(left, k - len(left) - len(right))

return pivot #answer




"""