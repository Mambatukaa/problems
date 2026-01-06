""""


Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) suchthat a * b = c * d where a, b, c, and d
are elements of nums, and a != b != c != d.

Example 1:
    Input: nums = [2,3,4,6]
    Output: 8

    Explanation: There are 8 valid tuples:
    (2,6,3,4), (2,6, 4,3), (6,2,3,4), (6,2,4,3),
    (3,4,2,6), (4,3,2,6), (3,4,6,2), (4,3,6,2).







Constraints:
• 1 <= nums.length <= 1000
• 1 <= nums[i] <= 10^4
• All elements in nums are distinct.

"""



class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def tupleSameProduct(self, nums) -> int:
        res = 0
        n = len(nums)
        counter = {}

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]

                counter[product] = counter.get(product, 0) + 1

                if counter[product] > 1:
                    res += 1


        return res * 8




nums = [2,3,4,6]

solution = Solution()

print("res:", solution.tupleSameProduct(nums))


