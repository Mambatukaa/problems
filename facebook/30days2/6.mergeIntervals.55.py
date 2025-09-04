""""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
class Solution:
    def merge(self, intervals):
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            first_interval = res[-1]
            second_interval = intervals[i]

            if first_interval[1] >= second_interval[0]:
                res[-1][1] = max(first_interval[1], second_interval[1])
            else:
                res.append(second_interval)

        return res
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for the result list
class Solution:
    def merge(self, intervals):

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
        
"""

to know overlap compare two intervals
    if first_interval[1] > second_interval[0]:
        merge
    else:
        add first_interval to the res








""" 




# Time Complexity: O(A + B)
# Space Complexity: O(A + B)
class Solution:
    def merge(self, A, B):
        # 2 pointers
        res = []

        p1 = 0
        p2 = 0

        def merge(res, interval):
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            # overlapped
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        while p1 < len(A) and p2 < len(B):
            interval = None

            # A started first
            if A[p1][0] < B[p2][0]:
                interval = A[p1]
                p1 += 1

            # B started first
            else:
                interval = B[p2]
                p2 += 1

            merge(res, interval)


        while p1 < len(A):
            merge(res, A[p1])
            p1 += 1

        while p2 < len(B):
            merge(res, B[p2])
            p2 += 1


        return res

#                         p1
A = [[3, 4], [5, 10], [11, 25]]
#               p2
B = [[2, 8], [10, 20]]



# res = [2, 20]

solution = Solution()

print("res:", solution.merge(A, B))
"""

A = [[3, 11], [14, 15], [18, 22]]
B = [[2, 8], [13, 20]]

"""
