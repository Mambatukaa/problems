# Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def mergeIntervals(intervals):
  res = []

  intervals.sort(key = lambda interval: interval[0], reverse = True)

  while len(intervals) > 1:
    first = intervals.pop()
    second = intervals.pop()

    # check these two intervals are overlap or not
    # overlap
    if first[1] >= second[0]:
      # merge it and add to the stack
      intervals.append([min(first[0], second[0]), max(first[1], second[1])])
    else:
      # add first one to the res and add second one to the stack
      res.append(first)
      intervals.append(second)


  if len(intervals):
    res.append(intervals.pop())


  return res

# Time Complexity: O(n log n)
# Space Complexity: O(n)
def mergeIntervalsII(intervals):
  intervals.sort(key = lambda interval: interval[0])
  merged = [intervals[0]]

  for i in range(1, len(intervals)):
    # overlapped
    if merged[-1][1] >= intervals[i][0]:
      merged[-1][1] = max(merged[-1][1], intervals[i][1])
    else:
      merged.append(intervals[i])

  return merged

intervals = [[2,6],[8,10],[15,18],[1,3]]

print("Res:", mergeIntervals(intervals))
intervals = [[2,6],[8,10],[15,18],[1,3]]
print("Res:", mergeIntervalsII(intervals))

"""

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].



"""
