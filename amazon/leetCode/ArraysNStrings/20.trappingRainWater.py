

# Time Complexity: O(n)
# Space Complexity: O(n)
def trap(height):
  n = len(height)

  maxLeft = [0] * n
  maxRight = [0] * n
  minLR = [0] * n

  currMax = 0

  for i in range(1, n):
    currMax = max(currMax, height[i - 1])
    maxLeft[i] = currMax

  currMax = 0

  for i in range(n - 2, -1, -1):
    currMax = max(currMax, height[i + 1])
    maxRight[i] = currMax

  for i in range(n):
    currMin = min(maxLeft[i], maxRight[i]) - height[i]
    minLR[i] = currMin if currMin > 0 else 0 

  return sum(minLR)

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print("res:", trap(height))


"""
Compute how much water it can trap after rain.


Formula = min(l, r) - h[i]


Find efficiently current element's left and right max.


Brute force: O(n^2)
  1. Iterate through height
    Check left right max on every iteration


OPTIMAL (maxLeft, maxRight, min(l,r)): Time Complexity: O(n)
                                       Space Complexity: O(n)

OPTIMAL (2 Pointers): Time Complexity: O(n)
                      Space Complexity: O(1)




"""
