from collections import deque

# Bfs
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
      m = len(grid)
      n = len(grid[0])


      #             BOTTOM    TOP     RIGHT   LEFT
      DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]


      def isValid(r, c, seen):
        return r >= 0 and r < m and c >= 0 and c < n and grid[r][c] != 0 and (r,c) not in seen

      def bfs(r, c, seen): 
        queue = deque([[r, c]])
        minutes = -1 

        while len(queue):
          size = len(queue)
          minutes += 1

          for i in range(size):
            [row, col] = queue.popleft()

            for [dx, dy] in DIRECTIONS:
              newRow = row + dx
              newCol = col + dy
  
              if isValid(newRow, newCol, seen):
                seen.add((newRow,newCol))
  
                queue.append([newRow, newCol])

        return minutes


      for r in range(m):
        for c in range(n):
          seen = set()
          # found rotten orange
          if grid[r][c] == 2:
            
            seen.add((r,c))
            minutes = bfs(r, c, seen)

            print(minutes, '-------------------')
            return minutes


"""

0 - empty cell
1 - fresh orange
2 - a rotten orange

Every minute 4-directionally adjacent to a rotten orange becomes rotten.

***************************************************************************

EXAMPLE 1:

grid = [
  [2, 1, 1],
  [1, 1, 0],
  [0, 1, 1]
]
dsaLeetCode/treesAndGraph/graph on  main [!?] via 
 5% ❯ ls
adjacencyList/                               adjacencyMatrix/                             allNodesDistancekInBT.js                     findIfPathExistsInGraph.js                   maxAreaOfIsland.js                           numberOfProvinces.js                         reachableNodesWithRestrictions.js
adjacencyList.js                             adjacencyMatrix.js                           canVisitAllRooms.js                          findSmallestSetOfVertices.js                 numberOfIslands.js                           reOrderRoutesToMakeAllPathsLeadToTheZero.js  shortestPathBinaryMatrix.js

dsaLeetCode/treesAndGraph/graph on  main [!?] via  v18.16.0
 5% ❯ cd ..

problems/dsaLeetCode/treesAndGraph on  main [!?] via  v18.16.0
 6% ❯ z neetcode

problems/neetCode150 on  main [!?]
 6% ❯ clear

problems/neetCode150 on  main [!?]
 6% ❯ ls
1.ArrayAndHashing/    10.heapPriorityQueue/ 11.graph/             2.TwoPointers/        3.Stack/              4.binarySearch/       5.slidingWindow/      6.linkedList/         7.trees/              8.trie/               9.backtracking/

problems/neetCode150 on  main [!?]
 6% ❯ clear
 25           if grid[r][c] == 2:
 24
 23             seen.add((r,c))
 22             minutes = bfs(r, c, seen)
 21
 20             print(minutes, '-------------------')
 19             return minutes
 18
 17
 16 """
 15
 14 0 - empty cell
 13 1 - fresh orange
 12 2 - a rotten orange
 11
 10 Every minute 4-directionally adjacent to a rotten orange becomes rotten.
  9
  8 ***************************************************************************
  7
  6 EXAMPLE 1:
  5
  4 grid = [
  3   [2, 1, 1],
  2   [1, 1, 0],
  1   [0, 1, 1]
68  ]
  1
  2 output: 4
  3
  4
  5 ***************************************************************************
  6
  7 EXAMPLE 2:
  8
  9 grid = [
 10   [2, 1, 1],
 11   [0, 1, 1],
 12   [1, 0, 1]
 13 ]
 14
 15 output: -1
 16 Explanation: The orange in the bottom left corner is never rotten because rotting only happens 4-directionally
 17
 18
 19 """
5.rottingOranges.994.py
Type  :qa  and press <Enter> to exit Nvim

output: 4


***************************************************************************

EXAMPLE 2:

grid = [
  [2, 1, 1],
  [0, 1, 1],
  [1, 0, 1]
]

output: -1
Explanation: The orange in the bottom left corner is never rotten because rotting only happens 4-directionally


"""
