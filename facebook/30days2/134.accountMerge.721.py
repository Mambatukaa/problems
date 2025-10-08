""""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 

Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.

"""

""""
accounts = [
    ["John","1","2"],
    ["John","3","1","4"],
    ["Mary","5"],
    ["John","6"]
]


adjacency_list

1: [2, 3]
2: [1]
3: [1, 4]
4: [3]
5:[]
6: []

name, node = account

John, 1


arr = []

dfs by neighbors and add node to the array

    arr.append(1)
        1: [2, 3, 4]

            2: arr.append(2)


"""

from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts):
        adj_list = defaultdict(list)

        for account in accounts:
            for i in range(2, len(account)):
                node1 = account[i]
                node2 = account[1]

                adj_list[node1].append(node2)
                adj_list[node2].append(node1)

        
        def dfs(node, arr):
            visited.add(node)
            arr.append(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, arr)


        res = []
        visited = set()

        # iterate through accounts group it by dfs
        for account in accounts:
            name = account[0]
            node = account[1]
            
            if node in visited:
                continue
            
            arr = []

            dfs(node, arr)

            res.append([name] + sorted(arr))

        return res

        



accounts = [
    ["John","1","2"],
    ["John","3","1","4"],
    ["Mary","5"],
    ["John","6"]
]

solution = Solution()
print("res:", solution.accountsMerge(accounts))
