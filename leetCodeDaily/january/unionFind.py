
# union find disjoint by rank

class UnionFind:

    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0


    def find(self, n):
        p = self.parent[n]

        # find the root parent
        while p != self.parent[p]:
            # optimization connect with grandparent
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        # cycle detected 
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1


        return True

unionFind = UnionFind(4)


print("res:", unionFind.union(2, 1))
print("res:", unionFind.union(2, 3))
print("res:", unionFind.union(3, 4))
print("res:", unionFind.union(4, 1))



