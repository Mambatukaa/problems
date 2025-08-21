"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

"""

class Solution:
    # Time Complexity: O(n^3)
    # Space Complexity: O(1)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                curr = nums[i] + nums[j]

                left = j + 1
                right = n - 1

                while left < right:
                    summ = curr + nums[left] + nums[right]

                    if summ == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1

                        while left < n and nums[left - 1] == nums[left]:
                            left += 1

                    elif summ > target:
                        right -= 1
                    else:
                        left += 1
        return res





        


"""
 0   1   2  3  4  5  6 
-2, -1, -1, 1, 1, 2, 2 ----- t = 0

i 
            j
               l
                     r


"""

class Solution:
    # Time Complexity: O(n^3) O(n^k-1)
    # Space Complexity: O(k) for recursion k can be same as n
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, quad = [], []
        nums.sort()


        def kSum(k, start, target):
            if k != 2:
                for i in range(start, n - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return

            left = start
            right = len(nums) - 1

            while left < right:
                summ = nums[left] + nums[right]

                if summ == target:
                    res.append(quad + [nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < n and nums[left] == nums[left - 1]:
                        left += 1

                elif summ > target:
                    right -= 1
                else:
                    left += 1

        kSum(4, 0, target)
        return res

# [-2, -1, 0, 0, 1, 2]