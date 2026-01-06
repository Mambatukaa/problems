"""









You are given a binary array nums.

You can do the following operation on the array any number of times (possibly zero):

Choose any 3 consecutive elements from the array and flip all of them.
Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

 

Example 1:

Input: nums = [0,1,1,1,0,0]

Output: 3

Explanation:
We can do the following operations:

Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].
Example 2:

Input: nums = [0,1,1,1]

Output: -1

Explanation:
It is impossible to make all elements equal to 1.

 

Constraints:

3 <= nums.length <= 105
0 <= nums[i] <= 1


"""

from collections import deque

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def minOperations(self, nums) -> int:
        n = len(nums)
        count = 0

        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = nums[i] ^ 1
                nums[i + 1] = nums[i + 1] ^ 1
                nums[i + 2] = nums[i + 2] ^ 1
                count += 1

        if nums[n - 2] == 0 or nums[n - 1] == 0:
            return -1

        return count

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def minOperationsII(self, nums) -> int:
        flip_queue = deque()
        count = 0

        for i in range(len(nums)):
            # Remove expired flips (older than 3 indices)
            while flip_queue and i > flip_queue[0] + 2:
                flip_queue.popleft()

            # If the current element needs flipping
            if (nums[i] + len(flip_queue)) % 2 == 0:
                # Cannot flip a full triplet
                if i + 2 >= len(nums):
                    return -1

                count += 1

                flip_queue.append(i)
            

        print(flip_queue)


        return count    
    
    # sliding window
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def minOperationsIII(self, nums) -> int:
        count = 0

        for i in range(2, len(nums)):
            if nums[i - 2] == 0:

                count += 1

                # flip the last 3 elements
                nums[i - 2] = nums[i - 2] ^ 1
                nums[i - 1] = nums[i - 1] ^ 1
                nums[i] = nums[i] ^ 1


        if sum(nums) == len(nums):
            return count


        return -1

solution = Solution()

nums = [0, 1, 1, 1, 0, 0]

print("res:", solution.minOperationsIII(nums))

