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


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def trap(self, height) -> int:
        n = len(height)

        leftMax = [0] * n
        rightMax = [0] * n
        min_vals = [0] * n

        curr_max = 0
        for i, hei in enumerate(height):
            curr_max = max(curr_max, hei)
            leftMax[i] = curr_max

        curr_max = 0

        for i in range(n - 1, -1, -1):
            hei = height[i]
            
            curr_max = max(curr_max, hei)
            rightMax[i] = curr_max


        for i in range(n):
            min_vals[i] = min(rightMax[i], leftMax[i])

        res = 0

        for i in range(n):
            res += max(0, min_vals[i] - height[i])


        return res


    # TWO POINTERS
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def trap(self, height) -> int:
        if not height:
            return 0
        n = len(height)

        left_max = height[0]
        right_max = height[n - 1]

        l = 0
        r = n - 1

        res = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])

                res += max(0, left_max - height[l])

            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += max(0, right_max - height[r])


        return res
                





solution = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print("res:", solution.trap(height))


