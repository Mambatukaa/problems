from collections import defaultdict, deque

# Time Complexity: O(q * (n + e)) q = queries. NOTE Building graph (n + e) the number of nodes plus the number of edges n + e
# Space Complexity: O(n + e) for building graph and seen
class Solution:
    def calcEquation(self, equations, values, queries):



      # build graph
      """
      a: { b: 1.5 }

      b: { a: 1 / 1.5, c: 2.5 }

      c: { b: 1 / 2.5 }

      bc: { cd: 5.0 }

      cd: { bc: 1 / 5  }

      """

      def answer_query(start, end):
        if start not in graph:
          return -1

        seen = {start}
        q = deque([[start, 1]])

        while q:
          node, ratio = q.popleft()

          if node == end:
            return ratio

          for neighbor in graph[node]:
            if neighbor not in seen:

              seen.add(neighbor)
              q.append([neighbor, ratio * graph[node][neighbor]])

        return -1



      graph = defaultdict(dict)

      # building the graph
      for i in range(len(equations)):
        start, end = equations[i]
        val = values[i]

        graph[start][end] = val
        graph[end][start] = 1 / val

      ans = []

      for start, end in queries:
        ans.append(answer_query(start, end))


      return ans

equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
values = [1.5, 2.5, 5.0]
queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]

solution = Solution()
print("res:", solution.calcEquation(equations, values, queries))
        
