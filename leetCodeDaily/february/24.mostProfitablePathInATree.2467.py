""""
There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0. You are given a 2D integer array edges
of length n - 1 where edges [i] = [ai, bil indicates that there is an edge between nodes ai and bi in the tree.
At every node i, there is a gate. You are also given an array of even integers amount, where amount [il represents:
• the price needed to open the gate at node i, if amount [i] is negative, or,
• the cash reward obtained on opening the gate at node i, otherwise.
The game goes on as follows:
• Initially, Alice is at node 0 and Bob is at node bob.
• At every second, Alice and Bob each move to an adjacent node. Alice moves towards some leaf node, while Bob moves
towards node 0.
• For every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward.
Note that:
• If the gate is already open, no price will be required, nor will there be any cash reward.
• If Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. In other
words, if the price to open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate
is c, both of them receive c / 2 each.
• If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 0, he stops moving. Note that these events
are independent of each other.
Return the maximum net income Alice can have if she travels towards the optimal leaf node.


Input: edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]
Output: 6

Explanation:
    The above diagram represents the given tree. The game goes as follows:
    - Alice is initially on node 0, Bob on node 3. They open the gates of their respective nodes.
    Alice's net income is now -2.
    - Both Alice and Bob move to node 1.
    Since they reach here simultaneously, they open the gate together and share the reward.
    Alice's net income becomes -2 + (4 / 2) = 0.
    - Alice moves on to node 3. Since Bob already opened its gate, Alice's income remains
    unchanged.
    Bob moves on to node 0, and stops moving.
    - Alice moves on to node 4 and opens the gate there. Her net income becomes 0 + 6 = 6.
    Now, neither Alice nor Bob can make any further moves, and the game ends.
    It is not possible for Alice to get a higher net income.


0: 1
1: 0, 2, 3
2: 1
3: 1, 4


"""


from collections import defaultdict, deque
# Time Complexity: O(n)
# Space Complexity: O(n)
# 2 DFS
class Solution:
    def __init__(self):
        self.bob_path = {}
        self.visited = []
        self.tree = defaultdict(list)
        self.max_income = float('-inf')


    def mostProfitablePath(self, edges, bob: int, amount) -> int:
        # build a tree
        for n1, n2 in edges:
            self.tree[n1].append(n2)
            self.tree[n2].append(n1)


        n = len(amount)

        self.visited = [False] * n

        self.find_bob_path(bob, 0)


        self.visited = [False] * n

        # source_node, time, income, amount
        self.find_alice_path(0, 0, 0, amount)

        return self.max_income



    def find_bob_path(self, source_node, time):
        self.visited[source_node] = True
        self.bob_path[source_node] = time

        if source_node == 0:
            return True

        for nei in self.tree[source_node]:
            if not self.visited[nei] and self.find_bob_path(nei, time + 1):
                return True

        # If node 0 isn't reached, remove current node from path
        del self.bob_path[source_node]

        return False
    
    def find_alice_path(self, source_node, time, income, amount):
        self.visited[source_node] = True

        if not source_node in self.bob_path or time < self.bob_path[source_node]:
            income += amount[source_node]
        elif time == self.bob_path[source_node]:
            income += amount[source_node] // 2

        # check the current node is leaf or not
        if source_node != 0 and len(self.tree[source_node]) == 1:
            self.max_income = max(self.max_income, income)

        for nei in self.tree[source_node]:
            if not self.visited[nei]:
                self.find_alice_path(nei, time + 1, income, amount)

                
# Time Complexity: O(n)
# Space Complexity: O(n)
# DFS BFS
class Solution:
    def __init__(self):
        self.bob_path = {}
        self.visited = []
        self.tree = defaultdict(list)
        self.max_income = float('-inf')


    def mostProfitablePath(self, edges, bob: int, amount) -> int:
        # build a tree
        for n1, n2 in edges:
            self.tree[n1].append(n2)
            self.tree[n2].append(n1)


        n = len(amount)

        self.visited = [False] * n

        self.find_bob_path(bob, 0)

        self.visited = [False] * n

        q = deque([[0, 0, 0]])

        while q:
            source_node, income, time = q.popleft()

            self.visited[source_node] = True

            if not source_node in self.bob_path or time < self.bob_path[source_node]:
                income += amount[source_node]
            elif time == self.bob_path[source_node]:
                income += amount[source_node] // 2

            if source_node != 0 and len(self.tree[source_node]) == 1:
                self.max_income = max(self.max_income, income)

            for nei in self.tree[source_node]:
                if not self.visited[nei]:
                    q.append([nei, income, time + 1])

        return self.max_income



    def find_bob_path(self, source_node, time):
        self.visited[source_node] = True
        self.bob_path[source_node] = time

        if source_node == 0:
            return True

        for nei in self.tree[source_node]:
            if not self.visited[nei] and self.find_bob_path(nei, time + 1):
                return True

        # If node 0 isn't reached, remove current node from path
        del self.bob_path[source_node]

        return False

edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3
amount = [-2,4,2,-4,6]

solution = Solution()

print("Res:", solution.mostProfitablePath(edges, bob, amount))
