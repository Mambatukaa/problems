from collections import deque

# BFS
# iterative
# Time Complexity: O(n)
# Space Complexity: O(n)
def jumpGameIII(arr, start):
  n = len(arr)
  seen = [False] * n

  seen[start] = True

  q = deque([start])

  while q:
    currIdx = q.popleft()

    if arr[currIdx] == 0:
      return True

    first = currIdx + arr[currIdx] 
    second = currIdx - arr[currIdx] 

    # add neighbors check neighbor is valid or not
    if first < n and seen[first] == False:
      seen[first] = True
      q.append(first)

    if second >= 0 and seen[second] == False:
      seen[second] = True
      q.append(second)

  return False

# DFS
# Recursive
# Time Complexity: O(n)
# Space Complexity: O(n)
def canReach(arr, start):
  n = len(arr)
  seen = [False] * n

  def helper(idx):
    if idx < 0 or idx >= n or seen[idx] == True:
      return False
    
    seen[idx] = True

    if arr[idx] == 0:
      return True

    return helper(idx + arr[idx]) or helper(idx - arr[idx])

  return helper(start)


arr = [4, 2, 3, 0, 3, 1, 2]
start = 0

print('res:', canReach(arr, start))


"""

non-negative inteegers

you can jump to i + arr[i] or i - arr[i]

       0  1  2  3  4  5  6
arr = [4, 2, 3, 0, 3, 1, 2]
start = 0


i = 0
  can jump 0 + arr[0] ===> 4
  can jump 0 - arr[0] ===> -4 not valid


i = 4
  can jump => 4 + arr[4] => 4 + 3 ===> 7 not valid
  can jump => 4 - arr[4] => 4 - 3 ===> 1


i = 1

  can jump => 1 + arr[1] => 1 + 2 ==> 3 GOTCHA arr[3] == 0 return TRUE



# GRAPH BFS problem

1. Add possible jumping idx to the queue starts from starting point
2. Add the neighbors until reach the 0
3. If q become empty return False


"""
