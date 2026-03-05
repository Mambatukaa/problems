""""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

"""

# TC: O(n)
# SC: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        
        for curr_day, curr_temp in enumerate(temperatures):
            # Pop until the current day's temperature is not
            # warmer than the temperature at the top of the stack
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        
        return answer

# TC: O(n)
# SC: O(1)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n

        hottest = 0

        for curr_day in range(n - 1, -1, -1):
            curr_temp = temperatures[curr_day]
            if curr_temp >= hottest:
                hottest = curr_temp
                continue
            
            days = 1

            while temperatures[curr_day + days] <= curr_temp:
                days += answer[curr_day + days]
            
            answer[curr_day] = days


        return answer

"""
hottes = 76
              c
                          d
  0   1   2   3   4   5   6   7
 73, 74, 75, 71, 69, 70, 76, 73

                  1   1   0   0

"""
