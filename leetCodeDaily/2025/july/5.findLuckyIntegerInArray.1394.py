""""
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.

 

Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
Example 3:

Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.
 

Constraints:

1 <= arr.length <= 500
1 <= arr[i] <= 500

"""
class Solution:
    def findLucky(self, nums: List[int]) -> int:
        # check the frequency is equal to the num
        # if there are many lucky numbers return the largest
        # if there is no lucky number return -1
        arr = [0] * 501

        for num in nums:
            arr[num] += 1

        for i in range(500, 0, -1):
            if arr[i] == i:
                return i

        return -1


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        from collections import Counter

        freq = Counter(arr)
        lucky = -1

        for num, count in freq.items():
            if num == count:
                lucky = max(lucky, num)

        return lucky
