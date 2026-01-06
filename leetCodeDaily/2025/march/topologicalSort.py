


class Solution:
    def topologicalSort(self, graph):
        self.stack = []
        self.visited = set()

        def dfs(node):
            self.visited.add(node)
            neighbors = graph[node]

            for neighbor in neighbors:
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    dfs(neighbor)

            self.stack.append(node)


        for node in graph:
            if node not in self.visited:
                dfs(node)

        
        while self.stack:
            print(self.stack.pop())

graph = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["H", "F"],
    "F": ["G"],
    "G": [],
    "H": []
}

solution = Solution()

print("res:", solution.topologicalSort(graph))
