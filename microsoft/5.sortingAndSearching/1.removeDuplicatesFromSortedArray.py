"""
Remove duplicates from sorted array

    idx = 4

                                 1
                                   2
    Input: nums = [0,1,2,3,2,2,3,3]
    Output: 5, nums = [0,1,2,3,_,_,_,_]



"""

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeDuplicates(self, nums):
        res = 1
        n = len(nums)

        if n == 1:
            return res

        p1 = 0
        p2 = 1

        while p2 < n:
            if nums[p1] != nums[p2]:
                # replace p1 + 1
                nums[p1 + 1] = nums[p2]
                res += 1

                p1 += 1
            p2 += 1

        return res

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeDuplicates(self, nums):
        insertIndex = 1
        size = len(nums)

        for i in range(1, size):
            if nums[i - 1] != nums[i]:
                nums[insertIndex] = nums[i]

                insertIndex += 1

        return insertIndex 







nums = [1, 1, 2]
solution = Solution()

print("res:", solution.removeDuplicates(nums))

print("modified nums:", nums)

