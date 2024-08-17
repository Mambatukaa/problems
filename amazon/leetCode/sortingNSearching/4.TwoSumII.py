# Time Complexity: O(n)
# Space Complexity: O(1)
def twoSumII(numbers, target):
  l = 0
  r = len(numbers) - 1

  while l <= r:
    currSum = numbers[l] + numbers[r]

    if currSum == target:
      return [l + 1, r + 1]
    elif currSum > target:
      r -= 1
    else:
      l += 1

  return []

numbers = [2, 7, 9, 11, 13, 14]

target = 9

print("res:", twoSumII(numbers, target))


"""
INPUT IS SORTED

numbers = [2, 7, 9, 11, 13, 14]

target = 9


output: [1, 2]

"""
