# helper function
def merge(nums, leftIdx, midIdx, rightIdx):
  leftArr = nums[leftIdx:midIdx]
  rightArr = nums[midIdx:rightIdx]

  l = r = 0
  k = leftIdx

  # replace nums leftIdx to rightIdx

  while l < len(leftArr) and r < len(rightArr):
    if leftArr[l] < rightArr[r]:
      nums[k] = leftArr[l]
      l += 1
    else:
      nums[k] = rightArr[r]
      r += 1

    k += 1

  while l < len(leftArr):
    nums[k] = leftArr[l]
    l += 1
    k += 1

  while r < len(rightArr):
    nums[k] = rightArr[r]
    r += 1
    k += 1


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

def mergeSort(nums, leftIdx, rightIdx):
  if leftIdx < rightIdx - 1:
    midIdx = leftIdx + (rightIdx - leftIdx) // 2

    # left half
    mergeSort(nums, leftIdx, midIdx)

    # right half
    mergeSort(nums, midIdx, rightIdx)

    merge(nums, leftIdx, midIdx, rightIdx)

nums = [6, 4, 3, 7, 5, 1, 2]

mergeSort(nums, 0, len(nums))

print("res:", nums)


"""

6, 4, 3, 7, 5, 1, 2


"""
