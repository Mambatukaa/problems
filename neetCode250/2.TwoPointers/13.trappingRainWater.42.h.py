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

# TC: O(n)
# SC: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        # move the min and update the answer
        # water = min(left, right) - current

        n = len(height)
        
        l = 0
        r = n - 1
        left_max = 0
        right_max = 0

        res = 0

        while l <= r:
            left_max = max(height[l], left_max)
            right_max = max(height[r], right_max)

            trap = 0
            if left_max <= right_max:
                trap = max(0,left_max - height[l])
                l += 1
            else:
                trap = max(0, right_max - height[r])
                r -= 1
            
            res += trap
         
        return res
