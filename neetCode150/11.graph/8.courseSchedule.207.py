# DFS
# Time Complexity: O(n)
# Space Complexity: O(n)
# Adjacency List
# NEETCODE
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      preMap = { i: [] for i in range(numCourses)}

      # build graph adjList
      for crs, pre in prerequisites:
        preMap[crs].append(pre)
      
      visited = set()

      def dfs(crs):
        if crs in visited:
          return False

        if preMap[crs] == []:
          return True
        
        visited.add(crs)

        for pre in preMap[crs]:
          if not dfs(pre): return False
          
        visited.remove(crs)
        preMap[crs] = []

        return True
        
      for crs in range(numCourses):
        if not dfs(crs): return False
      
      return True



"""

0: 1,
1: 0



prerequisites[i] = [ai, bi]


1. connections

Input: [[1, 0]]
Output: True



1. Visit every course until take the first course and after taking the course go back to the next course.
    During visit if we found circular break
    To catch circular track visited nodes




"""
