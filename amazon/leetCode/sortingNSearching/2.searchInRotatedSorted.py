"""

nums = [4, 5, 6, 7, 0, 1, 2]

target = 0

Output: 4


Constraints:
  • 1 <= nums. length <= 5000
  • -10^4 <= nums [i] <= 10^4
  • All values of nums are unique.
  • nums is an ascending array that is possibly rotated.
  • -10^4 <= target <= 10^4



Search target from nums. If found return idx of target.

array nums sorted in ascending order (with distinct values)....


Write an algorithm with O(log n) runtime complexity.

Binary Search!!!


 L        M        R
[4, 5, 6, 7, 0, 1, 2]

L = 4

M = 7

R = 2


L           M        R
7, 0, 1, 2, 3, 4, 5, 6


L = 7

M = 3

R = 6





(Left > Mid and Target < Mid):
   go left
else 
  go right



"""

# Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
def search(nums, target):

  l = 0
  r = len(nums) - 1

  while l <= r:
    m = l + (r - l) // 2

    if nums[m] == target:
      return m


    # mid belongs to left portion
    if nums[l] <= nums[m]:

      # go right
      if target > nums[m] or target < nums[l]:
        l = m + 1
      # go left
      else:
        r = m - 1

    # mid belongs to right portion
    else:
      # go left
      if target < nums[m] or target > nums[r]:
        r = m - 1
      else:
        l = m + 1

  return -1


#        0  1  2  3  4  5  6  7
#        L        M           R
#        T
nums =  [4, 5, 6, 7, 0, 1, 2, 3]
nums =  [7, 0, 1, 2, 3, 4, 5, 6]
nums = [3, 0]


print("res:", search(nums, 0))
