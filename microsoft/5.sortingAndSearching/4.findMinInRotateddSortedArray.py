"""
Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in 0 (log n) time.
"""

# Make decision to go left or right side of the array
# Time Complexity: O(log n)
# Space Complexity: O(1)
def findMin(nums):
    l = 0
    r = len(nums) - 1

    while l < r:
        mid = int((r - l) / 2 + l)

        if nums[mid] == nums[l] or nums[mid] == nums[r]:
            return min(nums[l], nums[r])

        if nums[l] < nums[mid] and nums[mid] > nums[r]:
            # go right
            l = mid
        else:
            r = mid

    return min(nums[l], nums[r])
# NeetCode solution that uses pivot to detect middle value belongs which sides of the array
# Time Complexity: O(log n)
# Space Complexity: O(1)
def findMinII(nums):
    res = nums[0]
    l = 0
    r = len(nums) - 1

    while l <= r:
        # check the array is already sorted or not
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        mid = int((r - l) / 2 + l)

        res = min(res, nums[mid])

        # check mid belongs to which part of the array
        # mid belongs to the left side and go to the right
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            # go to the left
            r = mid - 1

    return res

#             m
#       l
#                   r
nums = [4, 5, 1, 2, 3]

print("res:", findMinII(nums))

