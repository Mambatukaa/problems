# Time Complexity: O(log n)
# Space Complexity: O(n)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = (r - l) // 2 + l

            if ((mid == 0 or nums[mid] > nums[mid - 1]) and 
            (mid == n - 1 or nums[mid] > nums[mid + 1])):
               return mid
            
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1


        return -1






""""

    L 
  M
  R
1 2 3 1


        L
          M
            R
1 2 1 3 5 6 4]
0 1 2 3 4 5 6

   L
   M  
   R
1, 2
"""















# valley
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = (r - l) // 2 + l

            if ((mid == 0 or nums[mid] < nums[mid - 1]) and 
            (mid == n - 1 or nums[mid] < nums[mid + 1])):
               return mid
            
            if nums[mid] > nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1


        return -1






""""

    L 
  M
  R
1 2 3 1


        L
          M
            R
1 2 1 3 5 6 4]
0 1 2 3 4 5 6

   L
   M  
   R
1, 2
"""
        
