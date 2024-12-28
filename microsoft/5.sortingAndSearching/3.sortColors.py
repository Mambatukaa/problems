"""

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with
the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Constraints:

• n == nums. length
• 1 <= n <= 300
• nums lil is either 0, 1, or 2.


Follow up: Could you come up with a one-pass algorithm using only constant extra space?



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

"""


# Naive approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def sortColors(nums):
    count = [0, 0, 0]

    for idx in nums:
        count[idx] += 1


    """
    count = [2, 2, 2]
    
    """
    i = 0
    idx = 0

    while count:
        curr = count.pop(0)

        while curr > 0:
            nums[i] = idx
            i += 1
            curr -= 1

        idx += 1


nums = [0]
sortColors(nums)
print(nums)
