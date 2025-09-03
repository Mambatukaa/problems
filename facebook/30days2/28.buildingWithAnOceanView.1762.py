""""
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

 

Example 1:

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
Example 2:

Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.
Example 3:

Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.
 

Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 109




1. Keep track the right_max_val
2. If the current value is greater than the right_max_val add to the res

"""


# Time Complexity: O(n)
# Space Complexity: O(1) res 
class Solution:
    def findBuildings(self, heights):
        res = [len(heights) - 1]
        right_max_val = heights[-1]

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > right_max_val:
                res.append(i)
                right_max_val = heights[i]


        return res[::-1]

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Monotonic stack
    def findBuildings(self, heights):
        stack = []
        n = len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()

            stack.append(i)

        return stack



solution = Solution()
heights = [4,2,3,1]
heights = [4,3,2,1]
heights = [1,3,2,4]
print("res:", solution.findBuildings(heights))
            

# Time Complexity: O(n)
# Space Complexity: O(n)
# BOTH VIEW

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if len(heights) == 1:
            return heights


        l = 0
        r = len(heights) - 1

        left_max = heights[l]
        right_max = heights[r]

        left_view = [left_max]
        right_view = [right_max]
        
        res = []

        while l < r:
            if left_max < right_max:
                l += 1

                if left_max < heights[l] and l < r:
                    left_max = heights[l] 
                    left_view.append(left_max)
            else:
                r -= 1
                if right_max < heights[r] and l < r:
                    res.append(r)
                    right_max = heights[r] 
                    right_view.append(right_max)

        right_view.reverse()

        return left_view + right_view

        
