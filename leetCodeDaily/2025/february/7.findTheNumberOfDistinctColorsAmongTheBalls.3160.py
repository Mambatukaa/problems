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

    # With array
    def queryResults(self, limit: int, queries):
        n = len(queries)
        result = []
        color_map = {}
        ball_array = [0] * (limit + 1)

        # Iterate through queries
        for i in range(n):
            # Extract ball label and color from query
            ball, color = queries[i]

            # Check if ball is already colored
            if ball_array[ball] != 0:
                # Decrement count of the previous color on the ball
                prev_color = ball_array[ball]
                color_map[prev_color] -= 1

                # If there are no balls with previous color left, remove color from color map
                if color_map[prev_color] == 0:
                    del color_map[prev_color]

            # Set color of ball to the new color
            ball_array[ball] = color

            # Increment the count of the new color
            color_map[color] = color_map.get(color, 0) + 1

            result.append(len(color_map))

        return result


limit = 1
queries = [[0,1],[1,4],[1,1],[1,4],[1,1]]



solution = Solution()

print("res:", solution.queryResults(limit, queries))

