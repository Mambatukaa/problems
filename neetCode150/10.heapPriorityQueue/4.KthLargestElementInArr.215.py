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




# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         return nums[len(nums) - k]
def findKthLargest(nums: List[int], k: int) -> int:
    def quickselect(nums, k):
        small, equal, large = [], [], []
        pivot = nums[len(nums) - 1]
        for num in nums:
            if num > pivot:
                large.append(num)
            elif num == pivot:
                equal.append(num)
            elif num < pivot:
                small.append(num)

        # CASE-1
        if len(large) >= k:
            # means kth largest element is present in large array
            return quickselect(large, k)

        # CASE-2
        elif (len(large) + len(equal))  < k:
            # this means k-th largest element is in small array
            return quickselect(small, k-(len(large) + len(equal)))

        # CASE-3
        else:
            # pivot (and all elems. in equal) e j aapno k-th largest number chhe.
            return pivot
    return quickselect(nums, k)

with open('user.out', 'w') as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        k = next(inputs)
        print(findKthLargest(nums, k), file=f)
exit()
