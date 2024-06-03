# Time Complexity: O(n)
# Space Complexity: O(1)
# Greedy approach
class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
      # check their is possibility
      if sum(gas) < sum(cost):
        return -1
      

      # We have a valid answer
      start = 0
      total = 0

      for i in range(len(gas)):
        total += (gas[i] - cost[i])

        if total < 0:
          total = 0
          start = i + 1

      return start


      



solution = Solution()

gas = [5, 8, 2, 8]
cost = [6, 5, 6, 6]

print(solution.canCompleteCircuit(gas, cost))


"""
Find the starting point (IDX) that can circut once in the clockwise direction. If it's impossible return -1

1. sum(gas) must be greather than or equal to the sum(cost)

2. we cannot start from the negative difference. 
      Also if we reach negative number after starting the positive number that's invalid.
      We need to find the positive starting point that can reach the end with an positive total sum.



"""
        
