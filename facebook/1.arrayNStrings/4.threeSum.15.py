""""



Given an integer array nums, return all the triplets [nums [1], nums (il, nums[k]] suchthat i != j, i != k, and j != k, and nums [i] +
nums [j] + nums (k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]|
    Output: [[-1,-1,2] , [-1,8,1]]

Explanation:
    nums [0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums [1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums [0] + nums [3] + nums [4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.



Constraints:
• 3 <= nums.length <= 3000
• -10^5 <= nums [i] <= 10^5
"""



class Solution:
    # Naive approach 
    # Time Complexity: O(n^3)
    # Space Complexity: O(n)
    # TIME LIMIT EXCEEDED
    def threeSum(self, nums):
        res = []
        n = len(nums)
        seen = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    threeSum = nums[i] + nums[j] + nums[k]

                    
                    if threeSum == 0:
                        sumTuple = tuple(sorted([nums[i], nums[j], nums[k]]))

                        if sumTuple not in seen:
                            res.append([nums[i], nums[j], nums[k]])
                            seen.add(sumTuple)
        return res

    # Naive approach 
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    # Three pointers
    def threeSumII(self, nums):
        
        nums.sort()

        res = []
        n = len(nums)
        seen = set()

        for i in range(n):
            num1 = nums[i]
            l = i + 1
            r = n - 1

            while l < r:
                num2 = nums[l]
                num3 = nums[r]

                threeSum = num1 + num2 + num3

                if threeSum == 0:
                    sumTuple = (num1, num2, num3)

                    if sumTuple not in seen:
                        res.append([num1, num2, num3])
                        seen.add(sumTuple)
                    r -= 1
                    l += 1
                elif threeSum > 0:
                    # update right pointer
                    r -= 1
                else:
                    # update the left pointer
                    l += 1

        return res



nums = [-1,0,1,2,-1,-4]

solution = Solution()

print("res:", solution.threeSumII(nums))
