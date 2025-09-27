# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # just compare even mid with the next element
        # if they are same go right with r = mid + 2
        # else go left by 2

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if mid % 2:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                # go right. left sub array is in the right order
                l = mid + 2 # skipping the same number
            else:
                if nums[mid] != nums[mid - 1]:
                    return nums[mid]
                r = mid - 2

        return nums[l]


""""
       L
    M
        R
0 1 2 3 4 5 6 7 8
1 2 2 3 3 4 4 5 5


L
        M
                R
0 1 2 3 4 5 6 7 8
1 1 2 2 3 3 4 4 5

1. l = 0, m = 4, r = 8


"""

