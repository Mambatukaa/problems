"""
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.

 

Example 1:


Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
Example 2:


Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
Example 3:

Input: nestedList = [0]
Output: 0
 

Constraints:

1 <= nestedList.length <= 50
The values of the integers in the nested list is in the range [-100, 100].
The maximum depth of any integer is less than or equal to 50.

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
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

from typing import List
from collections import deque
# DFS
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    # DFS
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def depthSum(self, nestedList) -> int:
        def dfs(nested_list, depth):
            total = 0

            for item in nested_list:
                if isinstance(item, int):
                    total += item * depth
                else:
                    total += dfs(item, depth + 1)

            return total

        return dfs(nestedList, 1)
    # BFS
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    #
    def depthSumII(self, nestedList) -> int:
        q = deque(nestedList)
        total = 0
        depth = 1

        while q:
            for i in range(len(q)):

                item = q.popleft()

                if isinstance(item, int):
                    total += item * depth

                else:
                    for c in item:
                        q.append(c)

            depth += 1


        return total



            
nestedList = [1,[4,[6]]]
nestedList = [[1,1],2,[1,1]]
solution = Solution()

print("res:", solution.depthSumII(nestedList))
