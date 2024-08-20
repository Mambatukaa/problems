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


# Time Complexity: O(n log n)
# Space Complexity: O(n)
# NEETCODE
def minMeetingRoomsII(intervals):
  start = sorted([interval[0] for interval in intervals])
  end = sorted([interval[1] for interval in intervals])

  s, e = 0, 0

  res, counter = 0, 0

  while s < len(intervals):
    # if current meeting starts before the last meetng finish add room counts
    if start[s] < end[e]:
      s += 1
      counter += 1
    # if current meeting starts after the last meetng finish substract room counts
    else:
      e += 1
      counter -= 1

    res = max(res, counter)

  return res


intervals = [[0, 30], [5, 10], [10, 15]]

print("res:", minMeetingRoomsII(intervals))

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
