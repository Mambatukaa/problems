# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while maxDoubles > 0 and target > 1:
            if target % 2 == 1:
                count += 1
            target = target // 2
            maxDoubles -= 1
            count += 1

        return count + target - 1





# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
      if maxDoubles == 0:
        return target - 1
      
      curr = 0

      while target and maxDoubles:
        if target % 2 == 0:
          maxDoubles -= 1
          target //= 2
        else:
          target -= 1
        
        curr += 1

        if maxDoubles == 0:
          return curr + target - 1

      return curr - 1
        



""" 
Increment the current integer by one. x = x + 1
Double the current integer. x = x * 2

increment operations is limitless. 
double operation at most maxDoubles times.


Input: target = 19, maxDoubles = 2
    Initial x = 1

Minimum steps to reach the target ???????????

1. Is target integer or float?
    Integer

2. Initial x = 1 all the time? 
    Yes

3. Will x reach over target or exact?
    Exact target.



It looks like greedy approach?

EDGE CASES if maxDoubles == 0:
  return target - 1


Example 2:

  target = 19, maxDoubles = 2
  Output: 7

  Initial x = 1,
  Increment 3 times x = 4
  Double 1 time x = 8
  Increment 1 time  x = 9
  Double 1 time x = 18
  Increment 1 time x = 19 TARGET.........


  1. To find the good timing to double.

  Target = 19

    Try to mode by 2 it's possible?
      If yes. Decrease the maxDoubles.
      If no decrease by 1
    
    19 NO target = 18 maxDoubles = 2, 1
    18 YES target = 9 maxDoubles = 1, 2
    9 NO target = 8 maxDoubles = 1, 3
    8 YES target = 4 maxDoubles = 0, 4

    if maxDoubles === 0
      return current + target - 1;
    
    Time Complexity: O(n)
    Space Complexity: O(1)

    





"""
