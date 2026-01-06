""""


You are given a 0-indexed integer array nums. A pair of indices (i, j) isabad pairif i < jand j - i != nums[j] - nums [i].
Return the total number of bad pairs in nums.

Example 1:
    Input: nums = [4,1,3,3]
    Output: 5

    Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
    The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
    The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
    The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
    The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
    There are a total of 5 bad pairs, so we return 5.

Example 2:
    Input: nums = [1,2,3,4,5]
    Output: 0
    Explanation: There are no bad pairs.

Constraints:
• 1 <= nums.length <= 105
• 1 <= nums [i] <= 109



"""


class Solution:
    # Brute force
    # Time limit exceeded
    def countBadPairs(self, nums) -> int:
        res = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if j - i != nums[j] - nums[i]:
                    res += 1




        return res

    # Count totalPairs  and goodPairs
    # badPairs = totalPairs - goodPairs
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def countBadPairsII(self, nums):
        # j - i == nums[j] - nums[i] GOOD PAIRS
        totalPairs = 0
        goodPairs = 0
        diffMap = {}

        for pos in range(len(nums)):
            totalPairs += pos
            diff = pos - nums[pos]

            diffMap[diff] = diffMap.get(diff, 0)
            goodPairs += diffMap[diff]
            diffMap[diff] += 1

        
        return totalPairs - goodPairs

    def countBadPairsIII(self, nums):
        # j - i == nums[j] - nums[i] GOOD PAIRS
        diffMap = {}
        badPairs = 0

        for pos in range(len(nums)):
            diff = pos - nums[pos]

            goodPairsCount = diffMap.get(diff, 0)

            badPairs += pos - goodPairsCount

            diffMap[diff] = goodPairsCount + 1
        
        return badPairs



nums = [4, 1, 3, 3]

solution = Solution()

print("res:", solution.countBadPairsIII(nums))
            



        
