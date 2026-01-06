# Time Complexity: O(N * K log K) where N is the length of nums and K is the size of the subarray
# Space Complexity: O(K) for the frequency dictionary
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # k length subarray
        # x most frequent elements
        # calculate the x_sum
        n = len(nums)

        dic = {}

        res = []
        l = 0

        for r in range(n):
            dic[nums[r]] = dic.get(nums[r], 0) + 1
            # update the answer and remove the first element
            if r - l + 1 == k:
                # update the answer
                items = sorted(dic.items(), key=lambda x: (x[1], x[0]), reverse=True)

                res.append(sum(key * val for key, val in items[:x]))
                    
                dic[nums[l]] -= 1

                if dic[nums[l]] == 0:
                    del dic[nums[l]]
                l += 1


        return res

"""

1, 1, 2, 2, 3, 4, 2, 3 k = 6

1, 1, 2, 2, 3, 4 --> 1 + 1 + 2 + 2 = 6
   1, 2, 2, 3, 4, 2 --> 2 + 2 + 2 + 4 = 10
      2, 2, 3, 4, 2, 3


sliding window
    keep track of the frequency and get to x elements from the window




"""
        
