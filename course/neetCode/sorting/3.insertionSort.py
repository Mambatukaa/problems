
# First part is already sorted etc.
# Swap the current value until find the right position
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
def selectionSort(nums):
  n = len(nums)

  for i in range(1, n):
    while i > 0 and nums[i] < nums[i - 1]:
      # swap
      nums[i], nums[i - 1] = nums[i - 1], nums[i]
      i -= 1

  return nums

nums = [2, 3, 4, 1, 6]

print("res:", selectionSort(nums))
