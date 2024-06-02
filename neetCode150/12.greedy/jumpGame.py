# initial


"""
                 0  1  2  3  4
                 G     G  G  G
                 T  F  T  T
  Input: nums = [2, 0, 1, 1, 4]
  Output: True


  You are initially positioned at the array's first index. Each elements represents your max jump length at that position. Return true if you can reach the last index.


  GREEDY APPROACH
  GOAL STARTS FROM THE LAST ELEMENT
  1. Start to iterate from the backward. 
  2. Check the prev element can reach the GOAL.
        If can update the GOAL
        else check next element
  3. After checking each element and updating the GOAL check goal reach the first element or not.



  goalIdx = len(nums) - 1

  for i in range(len(nums) - 1, -1, -1):
    length = nums[i]

    if length + i >= GoalIdx:
      goalIdx = i


  return goalIdx == 0
    



"""


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
      goalIdx = len(nums) - 1

      for i in range(len(nums) - 1, -1, -1):
        length = nums[i]
    
        if length + i >= goalIdx:
          goalIdx = i
    
    
      return goalIdx == 0
  

