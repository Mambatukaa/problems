""""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 105





"""


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr) // 4

        for i in range(len(arr) - size):
            if arr[i] == arr[i + size]:
                return arr[i]
        return -1
        

# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = [arr[n // 4], arr[n // 2], arr[3 * n // 4]]

        size = n // 4

        for candidate in candidates:
            left = bisect_left(arr, candidate)

            if arr[left + size] == candidate:
                return candidate
        return -1

