""""

You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

 

Example 1:

    Input: nums = [3,2,3,2,2,2]
    Output: true
    Explanation: 
    There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
    If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

Example 2:

    Input: nums = [1,2,3,4]
    Output: false
    Explanation: 
    There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.
 

Constraints:
    nums.length == 2 * n
    1 <= n <= 500
    1 <= nums[i] <= 500

"""

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Hashmap
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for key in counter:
            if counter[key] % 2 == 1:
                return False
        return True

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Track unpaired numbers
        unpaired = set()

        # Add numbers to set if unseen, remove if seen
        for num in nums:
            if num in unpaired:
                unpaired.remove(num)
            else:
                unpaired.add(num)

        # Return true if all numbers were paired
        return not unpaired

# Time Complexity: O(n)
# Space Complexity: O(max_num)
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Find maximum value in array
        max_num = max(nums)

        # Toggle pair status for each number
        needs_pair = [False] * (max_num + 1)
        for num in nums:
            needs_pair[num] = not needs_pair[num]

        # Check if any number remains unpaired
        return not any(needs_pair[num] for num in nums)
solution = Solution()
