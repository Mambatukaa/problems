class UnionFind():
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0
            

    def find(self, node):
        p = self.par[node]

        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]

        self.par[node] = p
        return p


    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        # cycle found
        if p1 == p2:
            return False
        

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1

        return True






# Detect cycle
graph = [[1, 2], [2, 3], [3,4]]

unionFind = UnionFind(5)

print(unionFind.union(1, 3))
print(unionFind.union(2, 4))
print(unionFind.union(1, 2))
print(unionFind.union(4, 5))

print("parent:", unionFind.par)
print("rank", unionFind.rank)




"""


1 --> 2


"""
