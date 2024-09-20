# Divide and Conquer

def mergeSort(nums, s, e):
  if (e - s + 1 <= 1):
    return nums

  m = (s + e) // 2

  mergeSort(nums, s, m)
  mergeSort(nums, m + 1, e)

  merge(nums, s, m, e)

  return nums

nums = [3, 2, 4, 1, 6]

print("res:", mergeSort(nums, 0, len(nums) - 1))
