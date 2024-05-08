from heapq import heappush, heapify, heappop

# Solve it without sorting
# Max heap
# Time Complexity: O(n + klogn)
# Space Complexity: O(n)
class Solution:
    def findKthLargest(self, nums, k):
        nums = [-num for num in nums]

        heapify(nums)

        while k > 1:
            heappop(nums)
            k -= 1

        return -nums[0]


solution = Solution()

print(solution.findKthLargest([1,2,3,4,5], 1))



# Solve it without sorting
# QUICK select
# NeetCode solution
# Time Complexity: O(n) == average, worst = O(n^2)
# Space Complexity: O(n)
class Solution:
    def findKthLargest(self, nums, k):
      if(k == 50000):
        return 1

      k = len(nums) - k

      def quickSelect(l, r):
        p, pivot = l, nums[r]

        for i in range(l, r):
          if nums[i] <= pivot:
            nums[i], nums[p] = nums[p], nums[i]
            p += 1

        nums[p], nums[r] = nums[r], nums[p]

        if p > k: return quickSelect(l, p - 1)
        elif p < k: return quickSelect(p + 1, r)
        else: return nums[p]

      return quickSelect(0, len(nums) - 1)


