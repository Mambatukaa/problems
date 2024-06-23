class Solution:

    def maxArea(self, height) -> int:
      l = 0
      r = len(height) - 1

      res = 0

      while l <= r:
        leftHeight = height[l]
        rightHeight = height[r]
        res = max(res, min(leftHeight, rightHeight) * (r - l))

        if leftHeight < rightHeight:
          l += 1
        else:
          r -= 1

      return res


solution = Solution()

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(solution.maxArea(height))
"""

Brute Force. Time Complexity: O(n^2)


OPTIMAL SOLUTION 2 pointers Time Complexity: O(n)

Space Complexity: O(1)

          L                    R
          0  1  2  3  4  5  6  7
height = [1, 8, 6, 2, 5, 4, 3, 7]



RETURN MAXIMUM AMOUNT OF WATER A CONTAINER CAN STORE.



"""        
