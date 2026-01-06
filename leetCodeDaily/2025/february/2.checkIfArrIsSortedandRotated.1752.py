""""



Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including
zero). Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same length such that A[i] = B[(i+x) & A. length], where & is the
modulo operation.

Example 1:

    Input: nums = [3,4,5,1,2]
    Output: true
    Explanation: [1,2,3,4,5] is the original sorted array.
    You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

Example 2:
    Input: nums = (2,1,3,4]
    Output: false
    Explanation: There is no sorted array once rotated that can make nums.

"""



# Time Complexity: O(n)
# Space Complexity: O(1)
# Add solution comparing the adjacent elements
class Solution:
    def check(self, nums) -> bool:
        if len(nums) == 1:
            return False

        rotatedCount = 0
        nums.append(nums[0])

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                rotatedCount +=1 

                if rotatedCount > 1:
                    return False

        return True


nums = [3, 4, 5, 1, 2]
nums = [2,1,3,4]
nums = [1, 2, 3]

solution = Solution()

print("res:", solution.check(nums))
