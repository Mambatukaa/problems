""""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105













"""

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        

        res = 0

        left_heights = [0] * n
        right_heights = [0] * n 

        left_max = 0

        for i in range(n):
            left_heights[i] = left_max
            left_max = max(left_max, height[i])

        right_max = 0

        for i in range(n - 1, -1, -1):
            right_heights[i] = right_max
            right_max = max(right_max, height[i])

        res = 0

        for i in range(n):
            res += max(0, min(right_heights[i], left_heights[i]) - height[i])

        return res

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        ans = 0
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        return ans
