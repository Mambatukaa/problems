# Max value must be in the end


def selectionSort(nums):
  n = len(nums)

  for i in range(n):

    for j in range(0, n - i - 1):

      if nums[j] > nums[j + 1]:
        nums[j], nums[j + 1] = nums[j + 1], nums[j]

    print(nums)

  return nums


nums = [1, 5, 3, 2, 4]

print("res:", selectionSort(nums))
