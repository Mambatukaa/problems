""""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


"""


# Bucket sorting
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]

        count = Counter(nums)

        for num, v in count.items():
            buckets[v].append(num)

        res = []

        for bucket in buckets[::-1]:
            for num in bucket:
                res.append(num)

                if len(res) >= k:
                    return res
        
        return res



# TC: O(n + n log k) if k < n  O(N log N)
# SC: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        max_heap = []

        for num, v in count.items():
            heappush(max_heap, (-v, num))

        res = []

        while k > 0:
            res.append(heappop(max_heap)[1])
            k -= 1
        
        return res
