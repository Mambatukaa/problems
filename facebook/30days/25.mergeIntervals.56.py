""""


Given an array of intervals where intervals[il = [starti, endil, merge all overlapping
intervals, and return an array of the non-overlapping intervals that cover all the intervals in the
input.

Example 1:
    Input: intervals = [[1,31,[2,61,[8,101, [15,18]]
    Output: [[1,6], [8,10], [15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into
    [1,6] .

Example 2:
    Input: intervals = [[1,41,[4,511
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
• 1 < intervals.length <= 104
• intervals [i].length == 2
• 0 < starti < endi <= 104




"""
class Solution:
    # Time Complexity: O(n log n)
    # Space Complexity: O(log n) or O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for i in range(len(intervals) - 1):
            first = intervals[i]
            second = intervals[i + 1]

            # merge intervals
            if second[0] <= first[1]:
                intervals[i + 1] = [min(first[0], second[0]), max(first[1], second[1])]
            else:
                res.append(intervals[i])
        res.append(intervals[-1])

        return res






