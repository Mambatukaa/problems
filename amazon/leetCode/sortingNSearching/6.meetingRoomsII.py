from heapq import heappush, heappop, heapify


# Time Complexity: O(n log n)
# Space Complexity: O(n)
def meetingRoomsII(intervals):
  intervals.sort(key = lambda val: val[0])

  minHeap = []
  heapify(minHeap)
  res = 0

  for interval in intervals:

    while minHeap and minHeap[0] <= interval[0]:
      heappop(minHeap)

    heappush(minHeap, interval[1])

    res = max(res, len(minHeap))

  return res

intervals = [[1,2], [2,3]]

print("res:", meetingRoomsII(intervals))

"""


curr[1] <= new[0]:
  pop
else
  add
  update the answer


Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2


Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1



If there are any overlapped intervals that time we need extra room.


SOLUTION

Merge the intervals

Response will be the len(intervals) - len(mergedIntervals)


TO MERGE INTERVALS SORT THE INTERVALS

"""
