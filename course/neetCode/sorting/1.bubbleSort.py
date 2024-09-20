# Time Complexity: O(n^2)
# Space Complexity: O(1)
def bubbleSort(nums):
  n = len(nums)
  
  for i in range(n):
    isSorted = False

    for j in range(0, n - 1):
      if nums[j] > nums[j + 1]:
        nums[j], nums[j + 1] = nums[j + 1], nums[j]

        isSorted = True

    if not isSorted:
      break

  return nums


nums = [5, 4, 3, 2, 1]

print("Res:", bubbleSort(nums))

