""""
Given an array of positive integers arr (not necessarily distinct), return the lexicographically largest permutation that is smaller than arr, that can be made with exactly one swap. If it cannot be done, then return the same array.

Note that a swap exchanges the positions of two numbers arr[i] and arr[j]

 

Example 1:

Input: arr = [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.
Example 2:

Input: arr = [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.
Example 3:

Input: arr = [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.
 

Constraints:

1 <= arr.length <= 104
1 <= arr[i] <= 104









"""

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        # find the location
        n = len(arr)
        increasing_idx = n - 2

        for i in range(n - 1, -1, -1):
            if arr[increasing_idx] > arr[i]:
                break
            increasing_idx -= 1

        if increasing_idx == -1:
            return arr

        # find the closest smallest element
        j = n - 1
        for i in range(n - 1, increasing_idx, -1):
            if arr[j] >= arr[increasing_idx] or arr[j] == arr[j - 1]:
                j -= 1
        
        arr[j], arr[increasing_idx] = arr[increasing_idx], arr[j]

        return arr

        
        
