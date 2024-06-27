# Time Complexity: O(n^2)
# Space Complexity: O(n)
def threeSum(nums):
  nums.sort()
  n = len(nums)
  res = []

  for i in range(n):
    num = nums[i]

    if i > 0 and num == nums[i - 1]:
      continue

    l = i + 1
    r = n - 1

    while l < r:
      threeSum = num + nums[l] + nums[r]

      if threeSum == 0:
        res.append([num, nums[l], nums[r]])
        l += 1

        while nums[l] == nums[l - 1] and l < r:
          l += 1

      elif threeSum > 0:
        r -= 1
      else:
        l += 1
    

  return res


#nums = [ -1, -1, -1, 0, 1, 2, 4 ]
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]


print(threeSum(nums), 'ans')




"""

[nums[i], nums[j], nums[k]]

nums[i] + nums[j] + nums[k] === 0

i != j and i != k and j != k


nums = [ -1, 0, 1, 2, -1, 4 ]

output: [[-1, -1, 2], [-1, 0, 1]]


return distinct triplets..........


Brute Force
Time Complexity: O(n^3)



3 pointers

SORT
                 c  l     r   
nums = [ -1, -1, 0, 1, 2, 4 ]

-1, -1, 2


"""


