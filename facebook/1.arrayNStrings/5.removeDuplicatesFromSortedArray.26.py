""""


Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears
only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums .

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
    • Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in
    nums initially. The remaining elements of nums are not important as well as the size of nums .
    • Return K.

Custom Judge:

The judge will test your solution with the following code:

    intl] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length
    int k = removeDuplicates(nums); // Calls your implementation
    assert k == expectedNums. length;

    for (int i = 0; 1 < k; i++) {
        assert nums[il == expectedNums [il;
    }

If all assertions pass, then your solution will be accepted.



Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,__1_1_1_]

Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3,
    It does not matter what you leave beyond the returned k (hence they are underscores).


declare idx variable which track the unique elements position that is answer

compare nums[i] to nums[i - 1]

    if the values are the same don't do anything 
"""


# Time Complexity: O(n)
# Space Complexity: O(1)
def removeDuplicates(nums):
    idx = 1 

    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[idx] = nums[i]
            idx += 1

    return idx


#  idx:     i
#  i:             i
#       0 1 2 3 4 5 6 7 8 9
nums = [0,1,1,1,1,2,2,3,3,4]

print("res:", removeDuplicates(nums))
