# helper function
def merge(nums, left, right):
  # l = pointer for left arr, r = pointer for right arr, i = pointer for divided nums 
  l = r = i = 0

  # compare left and right and update nums
  while l < len(left) and r < len(right):

    # update nums by left
    if left[l] < right[r]:
      nums[i] = left[l]
      l += 1
    else:
      nums[i] = right[r]
      r += 1

    # update nums pointer
    i += 1

  # If the lengths of left and right are different, one side contains more items than the other.

  while l < len(left):
    nums[i] = left[l]

    l += 1
    i += 1

  while r < len(right):
    nums[i] = right[r]

    r += 1
    i += 1

# Time Complexity: O(N log N)
# Space Complexity: O(N) Sorting In Place: No Algorithm : Divide and Conquer
"""
Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation. 
  T(n) = 2T(n/2) + O(n) The solution of the above recurrence is O(nLogn). 
  The list of size N is divided into a max of Logn parts, and the merging of all sublists into a single list takes O(N) time, 
    the worst-case run time of this algorithm is O(nLogn) 
      Best Case Time Complexity: O(n*log n) 
      Worst Case Time Complexity: O(n*log n) 
      Average Time Complexity: O(n*log n) 
        The time complexity of MergeSort is O(n*Log n) in all the 3 cases (worst, average and best) as the mergesort always divides the array into two halves and takes linear time to merge two halves.


"""
def mergeSort(nums):

  # Divide if true
  if len(nums) > 1:
    mid = len(nums) // 2

    left = nums[:mid]
    right = nums[mid:]

    # Divide until false
    mergeSort(left)
    mergeSort(right)

    # Divide is finished then merge left and right

    merge(nums, left, right)





nums = [6, 4, 3, 7, 5, 1, 2]

mergeSort(nums)

print("res:", nums)


"""

6, 4, 3, 7, 5, 1, 2


"""
