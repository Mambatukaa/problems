class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            current = intervals[i]
            # merge
            if res[-1][1] >= current[0]:
                res[-1][1] = max(res[-1][1], current[1])
            else:
                res.append(current)

        return res
        
