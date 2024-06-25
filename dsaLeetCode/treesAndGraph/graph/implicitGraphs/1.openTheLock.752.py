from collections import deque

# Time Complexity: O(d) where d = deadends length. for converting deadends into a set. 
  # This is because everything else is constant. (4 slots, 10 digits)

# However if the lock had a variable number of slots, let's say n, then this changes 
  #our time complexity to O(10^n * n^2 + d). 

# There are 10^n different states because each slots has 10 options. 
  # At each state we perform, 

# O(n^2) work because we loop over the n slots while performing string concatenation, 
  # which is O(n) for immutable string.
  
# Space Complexity: O(4(d + 10^4))
def openTheLock(deadends, target):
  deadSet = set(deadends)

  q = deque(["0000"])

  turns = 0

  while q:
    for _ in range(len(q)):
      curr = q.popleft()

      if curr not in deadSet:
        deadSet.add(curr)

        if curr == target:
          return turns

        for i in range(4):
          x = int(curr[i])

          for diff in (-1, 1):
            y = (x + diff + 10) % 10

            neighbor = curr[:i] + str(y) + curr[i + 1:] 

            if neighbor in deadSet: 
              continue
            q.append(neighbor)

    turns += 1

  return -1



deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"

print('res:', openTheLock(deadends, target))

# To get neighbors, for each combination, we are looping 4 times (which is N) and in each iteration, there are subsring operations which costs O(N) => O(N^2)
class Solution:
    def openLock(self, deadends, target: str) -> int:
        def neighbors(code):
            for i in range(4):

                x = int(code[i])

                for diff in (-1, 1):
                    # NOTE
                    y = (x + diff + 10) % 10
                    yield code[:i] + str(y) + code[i + 1:]

        deadSet = set(deadends)
        if "0000" in deadSet: return -1
        q = deque(["0000"])
        steps = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return steps
                for nei in neighbors(curr):
                    if nei in deadSet: continue
                    deadSet.add(nei)  # Marked as visited
                    q.append(nei)
            steps += 1

        return -1

solution = Solution()

print(solution.openLock(deadends, target))

# add possible neighbors to the queue
"""
0000
  1000
  0100
  0010
  0001
  9000
  0900
  0090
  0009
"""
