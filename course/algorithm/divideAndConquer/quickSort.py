
# Time Complexity: O(N log N)... Worst: O(n^2)
# Space Complexity: O(n) Unlike merge sort

"""
Choose pivot number and locate smaller numbers at the left of the pivot and larger numbers at the right of the pivot.

"""


def partition(nums, start, end):
  pivot = end
  i = start - 1

  for j in range(start, end + 1):
    if nums[j] <= nums[pivot]:
      i += 1
      nums[j], nums[i] = nums[i], nums[j]

  return i

# Time Complexity: O(N log N)
# Space Complexity: O(n)
def quickSort(nums, start, end):
  if start < end:
    pivot = partition(nums, start, end)

    # left sub array
    quickSort(nums, start, pivot - 1)

    # right sub array
    quickSort(nums, pivot + 1, end)

nums = [3, 5, 8, 1, 2, 9, 4, 7, 6]

quickSort(nums, 0, len(nums) - 1)

print("res:", nums)
