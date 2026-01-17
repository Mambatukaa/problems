""""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
"""

# SC: O(n)
# TC: O(n)
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N - 1:
            return -1
        
        indegree = [0] * (N + 1)
        outdegree = [0] * (N + 1)
        
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
            
        for i in range(1, N + 1):
            if indegree[i] == N - 1 and outdegree[i] == 0:
                return i
        return -1 
