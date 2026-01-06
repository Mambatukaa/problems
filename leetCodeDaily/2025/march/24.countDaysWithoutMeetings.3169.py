class Solution:
    # Sorting
    def countDays(self, days: int, meetings) -> int:

        n = len(meetings)
        meetings.sort(key=lambda x: x[0])

        merged_meetings = []

        for i in range(n - 1):
            first_start, first_end = meetings[i]
            second_start, second_end = meetings[i + 1]

            # unmergeable
            if first_end < second_start:
                merged_meetings.append(meetings[i])
            else:
                meetings[i + 1] = [first_start, max(first_end, second_end)]

        merged_meetings.append(meetings[-1])

        if len(merged_meetings) == 1:
            start = merged_meetings[0][0]
            end = merged_meetings[0][1]

            return (days - end) + start - 1



        for start, end in merged_meetings:
            for i in range(start, end + 1):
                days -= 1
        return days


from collections import defaultdict
        
class Solution:
    # Time Complexity: O(n log n)
    # Space Complexity: O(log n) or O(n) sorting space required
    def countDays(self, days: int, meetings) -> int:
        free_days = 0
        latest_end = 0

        meetings.sort()

        for start, end in meetings:
            if start > latest_end + 1:
                free_days += start - latest_end - 1

            latest_end = max(latest_end, end)

        return days - latest_end + free_days





# Line sweep
# Time Complexity: O(n log n)
# Space Complexity: O(n) or O(log n)
class Solution:
    def countDays(self, days: int, meetings) -> int:
        free_days = 0
        days_map = defaultdict(int)
        prefix_sum = 0
        previous_day = days

        for start, end in meetings:
            days_map[start] += 1
            days_map[end] -= 1

            previous_day = min(previous_day, start)

        free_days += previous_day - 1

        for current_day in sorted(days_map.keys()):

            # update the answer
            if prefix_sum == 0:
                free_days += current_day - previous_day - 1

            prefix_sum += days_map[current_day]
            previous_day = current_day

        free_days += days - previous_day + 1

        return free_days



solution = Solution()

days = 10
meetings = [[2, 4], [8, 9]]

print("res:", solution.countDays(days, meetings))
