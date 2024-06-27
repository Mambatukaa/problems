# Time Complexity: O(n^2)
# Space Complexity: O(n)
def threeSum(nums):
  nums.sort()
  n = len(nums)
  seen = set()

  for i in range(n):
    num = nums[i]

    l = i + 1
    r = n - 1

    while l < r:
      threeSum = num + nums[l] + nums[r]

      if threeSum == 0:
        seen.add((num,nums[l],nums[r]))
        r -= 1
        l += 1
      elif threeSum > 0:
        r -= 1
      else:
        l += 1
    
  res = []

  for s in seen:
    res.append([s[0], s[1], s[2]])

  return res


nums = [ -1, -1, 0, 1, 2, 4 ]
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


