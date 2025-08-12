""""
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
 

Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.



each rows and columns sorted





"""



from heapq import heappush, heappop

from typing import List


"""
Time Complexity: let X=min(K,N);X+Klog(X)

Well the heap construction takes O(X) time.
After that, we perform K iterations and each iteration has two operations. We extract the minimum element from a heap containing X elements. Then we add a new element to this heap. Both the operations will take O(log(X)) time.
Thus, the total time complexity for this algorithm comes down to be O(X+Klog(X)) where X is min(K,N).
Space Complexity: O(X) which is occupied by the heap.


"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []

        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(min(k, ROWS)):
            # value, row, col
            heappush(min_heap, (matrix[r][0], r, 0))

        while k != 0:
            element, row, col = heappop(min_heap)

            if col + 1 < COLS:
                heappush(min_heap, (matrix[row][col + 1], row, col + 1))

            k -= 1

        return element