"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length


"""
# Time Complexity: O(n)
# Space Complexity: O(k) maximum k elements in queue
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([0])
        res = []

        # first window
        for i in range(1, k):
            curr = nums[i]
            # remove the elements that less than curr
            while queue and nums[queue[-1]] <= curr:
                queue.pop()

            # add curr element
            queue.append(i)
        
        # add first element to the queue
        res.append(nums[queue[0]])

        for i in range(k, len(nums)):
            curr = nums[i]
            # remove the elements that less than curr
            while queue and nums[queue[-1]] <= curr:
                queue.pop()

            # add curr element
            queue.append(i)

            if queue[0] <= i - k:
                queue.popleft()

            res.append(nums[queue[0]])

        return res

            


"""

0  1   2  3  4  5  6  7
1  3  -1 -3  5  3  6  7
       p

queue = [3]

1. Remove the elements that less than current from the queue
2. Add curr element to the queue
3. queue[0] will be always the max element
4. If queue[0] is not in the current window popleft()



"""
