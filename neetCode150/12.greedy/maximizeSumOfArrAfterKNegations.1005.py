from heapq import heappop, heappush, heapify

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
      heapify(nums)

      while k:
        item = heappop(nums)
        heappush(nums, -item)
        k -= 1
    
      return sum(nums)






      



"""
heap or sort


heapify the nums and change first element by -nums[i] k times


"""
        
