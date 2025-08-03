# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                if nums[l] <= target or nums[l] > nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[r] >= target or nums[r] < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1


        return -1    

        
"""

                t
    l        m     r
 0  1  2  3  4  5  6
[4, 5, 6, 7, 0, 1, -1]

t = 0
"""
