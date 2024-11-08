

# Time Complexity: O(n)
# Space Complexity: O(n)
def trap(height):
  n = len(height)

  leftMax = [0] * n 
  rightMax = [0] * n

  # calculate the leftMax elements
  for i in range(1, n):
    leftMax[i] = max(height[i - 1], leftMax[i - 1])

  # calculate the rightMax elements
  for i in range(n - 2, -1, -1):
    rightMax[i] = max(height[i+1], rightMax[i + 1])

  res = 0

  for i in range(n):
    # formula trap[i]
    res += max(0, min(leftMax[i], rightMax[i]) - height[i])

  return res


# Time Complexity: O(n)
# Space Complexity: O(1)
def trapII(height):
  n = len(height)

  leftMax, rightMax = 0, 0

  left, right = 0, n - 1
  ans = 0

  while left <= right:
    if height[left] < height[right]:
      if leftMax > height[left]:
        # update the answer
        ans += leftMax - height[left]
      else:
        leftMax = height[left]
      left += 1

    else:
      if rightMax > height[right]:
        ans += rightMax - height[right]
      else:
        rightMax = height[right]

      right -= 1


  return ans             



height = [0,1,0,2,1,0,1,3,2,1,2,1]

print("Res:", trap(height))
print("ResII:", trapII(height))




"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.




Start to iterate from 0th idx
  Calculate the water can track on the idx. And increase the res.
    Two calculate the water use two pointers to know left right max value.


"""
