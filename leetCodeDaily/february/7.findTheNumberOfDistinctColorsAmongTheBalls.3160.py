""""

You are given an integer limit and a 2D array queries of size n x 2.
There are limit + 1 balls with distinct labels in the range [0, limit] . Initially, all balls are uncolored. For every query in queries that is of
the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.
Return an array result of length n, where result [1] denotes the number of distinct colors after ith query.
Note that when answering a query, lack of a color will not be considered as a color.

Example 1:
Input: limit = 4, queries = [[1,4), (2,5], [1,3), [3,4]]
Output: [1,2,2,3]


Constraints:
• 1 <= limit <= 109
• 1 <= n == queries.length <= 105
• queries (i].length == 2
• 0 <= queries(i][0] <= limit
• 1 <= queries[i][1] <= 10^9
"""


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Two hashmaps
    def queryResults(self, limit: int, queries):
        ballsMap = {}
        colorsMap = {}
        res = []

        for x, y in queries:
            if x in ballsMap:
                # update color map
                prevCol = ballsMap[x]

                colorsMap[prevCol] -= 1

                if colorsMap[prevCol] == 0:
                    del colorsMap[prevCol]

            ballsMap[x] = y
            colorsMap[y] = colorsMap.get(y, 0) + 1

            res.append(len(colorsMap))

        return res



limit = 1
queries = [[0,1],[1,4],[1,1],[1,4],[1,1]]



solution = Solution()

print("res:", solution.queryResults(limit, queries))

