
def merge(nums1, m, nums2, n):
    #empty slot



nums1 = [1,2,3,0,0,0,0]
m = 3
nums2 = [2,2,5,6]
n = 4
merge(nums1, m, nums2, n)
print("res:", nums1)


"""


You are given two integer arrays nums1 and nums, sorted in non-decreasing order, and two integers m and n, representing the
number of elements in nums and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.


The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this,
nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are
set to 0 and should be ignored. nums2 has a lengthof n.

Example 1:

    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]

Explanation: The arrays we are merging are [1,2,31 and [2,5,6].

The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


Follow up: Can you come up with an algorithm that runs in O(m + n) time?



compare the values and make decisions 
    if nums1[i] < nums[j] update the i pointer:


    else:
        replace nums1[i] by nums2[j] and replace the first empty spot by nums1[i] and increase the j and i pointer

"""
