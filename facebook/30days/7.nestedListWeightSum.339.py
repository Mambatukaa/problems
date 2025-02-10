"""

You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other
lists.
The depth of an integer is the number of lists that it is inside of. For example, the nested list [1, (2,2], 1[31,2], 1] has each integer's
value set to its depth.
Return the sum of each integer in nestedList multiplied by its depth.



Input: nestedList = [[1,1],2, [1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.




Constraints:
• 1 <= nestedList. length <= 50
• The values of the integers in the nested list is in the range [-100, 100].
• The maximum depth of any integer is less than or equal to 50.

"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

from collections import deque
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # DFS
    def depthSum(self, nestedList) -> int:
        def dfs(nested, depth):
            res = 0

            for item in nested:
                if type(item) == int:
                    res += item * depth
                else:
                    res += dfs(item, depth + 1)

            return res
    
        return dfs(nestedList, 1)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # BFS
    def depthSumII(self, nestedList) -> int:
        res = 0
        q = deque([[nestedList, 1]])

        while q:
            nested, depth = q.popleft()

            for item in nested:
                if type(item) == int:
                    res += item * depth
                else:
                    q.append([item, depth + 1])

        return res

solution = Solution()

nestedList = [[1,1],2,[1,1]]

print("res:", solution.depthSum(nestedList))
print("res 2:", solution.depthSumII(nestedList))


        
