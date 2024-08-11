# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# Naive solution used iteration
def findMedianSortedArrays(nums1, nums2):
  l = 0
  r = 0

  arr = []

  while l < len(nums1) and r < len(nums2):

    if nums1[l] < nums2[r]:
      arr.append(nums1[l])
      l += 1
    else:
      arr.append(nums2[r])
      r += 1


  arr = arr + nums1[l:] + nums2[r:]

  n = len(arr)

  if not n:
    return -1

  mid = n // 2

  if n % 2 == 1:
    return arr[mid]

  # 1 2 3 4
  # 1, 2

  return (arr[mid] + arr[mid - 1]) / 2



# The overall run time complexity should be O(log (m+n)).

# Time Complexity: O(log (m + n))
# Space Complexity: O(log (m + n))
# Optimal solution using binary search

def findMedianSortedArraysII(nums1, nums2):

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

print("res:", findMedianSortedArraysII(nums1, nums2))

"""

Constraints:
  • nums1.length == m
  • nums2.length == n
  • 0 <= m ＜= 1000
  • 0 <- n <= 1000
  • 1 <= m + n <= 2000
  • -10^6 <= nums1[i], nums2[i] <= 10^6


merge the sorted array and find median.

MEDIAN MIDDLE ELEMENT OF SORTED ARRAY.
  If array has even elements median will be average of the middle two elements.



1. Merge the two lists
2. If length is even return average of two middle elements
   else return middle element


Time Complexity: O(n + m)
Space Complexity: O(n + m)

"""

