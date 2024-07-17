from collections import defaultdict, deque
import string

# Time Complexity: O(n)
# Space Complexity: O(n)
# DFS
def equationsPossible(equations):
  graph = defaultdict(set)
  notEquals = []

  def canMeet(a, b, seen):
    if a == b:
      return True

    seen.add(a)

    for neighbor in graph[a]:
      if neighbor in seen:
        continue

      if canMeet(neighbor, b, seen):
        return True

    return False

  for equation in equations:
    a = equation[0]
    b = equation[3]
    e = equation[1]

    if e == "!":
      notEquals.append((a,b))
      continue

    graph[a].add(b)
    graph[b].add(a)

  for a,b in notEquals:
    if canMeet(a, b, set()):
      return False

  return True

# BFS
def equationsPossibleII(equations):
  graph = defaultdict(set)
  notEquals = []

  for a, e, _, b in equations:
    if e == "!":
      notEquals.append((a,b))
      continue
    
    # since they are equal add a node on each nodes
    graph[a].add(b)
    graph[b].add(a)

  # search target from a neighbors and also their neighbors
  def bfs(a, target):
    seen = set()
    seen.add(a)

    q = deque([a])

    while q:
      curr = q.popleft()

      if curr == target:
        return True

      for neighbour in graph[curr]:
        if neighbour in seen:
          continue
        q.append(neighbour)
        seen.add(neighbour)

  # check not equals node can meet
  for a,b in notEquals:
    if bfs(a, b):
      return False

  return True

equations = ["b==a", "b!=c", "c==a"]

print("res:", equationsPossibleII(equations))

"""

Input: equations = ["a==b", "b!=a"]
Output: False

********************************************************************************

Input: equations = ["a==b", "b==a"]
Output: True


Constraints:
  equations[i][0] and equations[i][3] lowercase english letters
  equations[1] is either '=' or '!'
  equations[2] is '='


Union Find Solution

We will store variables in same component if they are equal.
Then we will check non-equality equtions, if both variables in any of those equation are in same component, we return false.


STEP 1: ==
  Create components of all equations.

STEP 2: !=
  Check if they are part of the same component, then return false


DFS

"""
