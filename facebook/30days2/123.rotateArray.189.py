"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?



"""
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        n = len(nums)

        k %= n

        # reverse original nums
        reverse(nums, 0, n - 1)

        # reverse the k portion
        reverse(nums, 0, k - 1)

        # reverse the remaining
        reverse(nums, k, n - 1)

"""

1. pop elements last time and append to the array 0th index O(N^2)
2. Reverse the nums and reverse the k portion and remaining portion

 0 1 2 3 4 5 6
[1,2,3,4,5,6,7], k = 3
                 k = 15
                 k = 33



"""       
        
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)


        while k:
            nums.insert(0, nums.pop())
            k -= 1


# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        res = [0] * n
        k %= n

        for i in range(n):
            res[(i + k) % n] = nums[i]


        nums[:] = res



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        start = count = 0

        while count < n:
            curr_idx, prev_num = start, nums[start]

            while True:
                next_idx = (curr_idx + k) % n
                nums[next_idx], prev_num = prev_num, nums[next_idx]
                count += 1

                curr_idx = next_idx

                if start == curr_idx:
                    break
            start += 1




"""

k = 3

0  1  2  3  4  5  6
1, 2, 3, 4, 5, 6, 7

1, 2, 3, [1], 5, 6, [4]
1, 2, [7], [1], 5, [3], [4]
1, [6], [7], [1], 5, [3], [4]
1, [6], [7], [1], [2], [3], [4]
[5], [6], [7], [1], [2], [3], [4]

1. track prev element and replace the next element which is (i + k) % n
2. Swap will happen n times
3.


0  1  2  3
1, 2, 3, 4 k = 2

1, 2, [1], 4
[3], 2, [1], 4


1 2 3 4
1 2 .1 4

.3 2 .1 4

.3 .4 .1 .2


1 2 3 4 5

1 2 .1 4 .3
1 .3 .1 .2. 3

.4

"""
