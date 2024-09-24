def merge(nums, left, mid, right):
  # left l: mid
  # right mid:r
  leftArr = []
  rightArr = []

  print(left, right)

  for i in range(left, mid):
    leftArr.append(nums[i])

  for j in range(mid, right):
    rightArr.append(nums[j])

  l = 0
  r = 0

def mergeSort(nums):
  # base case
  if len(nums) > 1:
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    # divide
    mergeSort(left)
    mergeSort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        nums[k] = left[i]
        i += 1
      else:
        nums[k] = right[j]
        j += 1

      k += 1

    while i < len(left):
      nums[k] = left[i]
      i += 1
      k += 1

    while j < len(right):
      nums[k] = right[j]
      j += 1
      k += 1


nums = [6, 4, 3, 7, 5, 1, 2]

mergeSort(nums)

print("res:", nums)


"""

6, 4, 3, 7, 5, 1, 2

[6, 4, 3, 7] [5, 1, 2]

[6, 4] [3 7] [5, 1] [2]

[6] [4] [3] [7] [5] [1] [2] ----------------- Start to merge

[4, 6] [3, 7] [1, 5], [2]

[3, 4, 6, 7] [1, 2, 5]

[1, 2, 3, 4, 5, 6, 7]


"""
