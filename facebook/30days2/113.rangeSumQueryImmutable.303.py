"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange.


"""
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
        

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [nums[0]]

        for num in nums[1:]:
            last_num = self.prefix[-1]
            self.prefix.append(last_num + num)
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        
        return self.prefix[right] - self.prefix[left - 1]
        

"""
 0. 1. 2. 3. 4. 5
[1, 2, 3, 4, 5, 6]

0  1  2  3   4   5
1, 3, 6, 10, 15, 21

if left == 0:
    return prefix[right]
else:
    return prefix[right] - prefix[left - 1]


range(0, 2) --> 1 + 2 + 3 = 6
range(1, 2) --> 2 + 3 = 5

range(2, 4) --> 3 + 4 + 5 = 12


"""

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
