class Solution:
    # Two pointers solution
    # Time Complexity: O(n log n)
    # Space Complexity: O(n log n or n)
    def countFairPairs(self, nums, lower: int, upper: int) -> int:
        nums.sort()

        def found_pairs(value):
            l = 0
            r = len(nums) - 1

            res = 0

            while l < r:
                curr_sum = nums[l] + nums[r]

                if curr_sum < value:
                    res += r - l
                    l += 1

                else:
                    r -= 1
            return res

        return found_pairs(upper + 1) - found_pairs(lower)

    # Two pointers solution
    # Time Complexity: O(n log n)
    # Space Complexity: O(n log n or n)
    def countFairPairsII(self, nums, lower: int, upper: int) -> int:
        nums.sort()


        # find number of counts that less than 
        def binary_search(l, r, element):
            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] >= element:
                    r = mid - 1
                else:
                    l = mid + 1

            return l

        
        res = 0

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            low = binary_search(l, r, lower - nums[i])
            high = binary_search(l, r, upper - nums[i] + 1)

            res += high - low


        return res
            

""""

2 pointers



binary search solutions

        #                r
        #          l
        #       c
        # 0  1  2  3  4  5
        # 0, 1, 4, 4, 5, 7 lower = 3, upper = 6 
        # el = 3
        
        low = 2
        high = 5

        1:
         low = 2 
         high = 5
        2:
        

"""
