""""



An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
You are given an array of integers nums . Return true if nums is a special array, otherwise, return false.

Example 1:
Input: nums = [1]
Output: true
Explanation:
There is only one element. So the answer is true.


"""



class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def isOdd(num):
            return num % 2 == 1

        for i in range(len(nums) - 1):
            if isOdd(nums[i]) == isOdd(nums[i + 1]):
                return False

        
        return True

        


# Bitwise
class Solution:
    def isArraySpecial(self, nums):
        # Iterate through indexes 0 to n - 1
        for index in range(len(nums) - 1):

            # Compare the parities using bitwise operations
            if ((nums[index] & 1) ^ (nums[index + 1] & 1)) == 0:

                # If the two adjacent numbers have the same parity, return False
                return False

        # Return True if no pair of adjacent numbers with the same parity are found
        return True
