# Time Complexity: O(n)
# Space Complexity: O(1)
def waysToSplitArray(nums):
    res = 0
    totalSum = 0

    for num in nums:
        totalSum += num

    leftSum = nums[0]
    rightSum = totalSum - leftSum

    for i in range(1, len(nums)):
        if leftSum >= rightSum:
            res += 1

        leftSum += nums[i]
        rightSum -= nums[i]

    return res

nums = [10, 7, 100]

print("res:", waysToSplitArray(nums))


"""

You are given a O-indexed integer array nums of length n.
nums contains a valid split at index i if the following are true:

• The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1
elements.
• There is at least one element to the right of i. That is, o < i < n - 1.
Return the number of valid splits in nums.




  i
[10, 4, -8, 7]

"""
