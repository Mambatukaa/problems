from typing import List

import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:


        # quick sort

        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
        def quickSort(nums):
            if len(nums) <= 1:
                return nums


            pivot = random.choice(nums)

            left = []
            mid = []
            right = []

            for num in nums:
                if num < pivot:
                    left.append(num)
                elif num == pivot:
                    mid.append(num)
                else:
                    right.append(num)

            return quickSort(left) + mid + quickSort(right)
        
        # Time complexity: O(n log n)
        # Space complexity: O(n)
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = arr[:mid]
            right = arr[mid:]

            sorted_left = merge_sort(left)
            sorted_right = merge_sort(right)

            return merge(sorted_left, sorted_right)
        
        def merge(left, right):
            sorted_list = []

            p1 = 0
            p2 = 0

            while p1 < len(left) and p2 < len(right):
                if left[p1] < right[p2]:
                    sorted_list.append(left[p1])
                    p1 += 1
                else:
                    sorted_list.append(right[p2])
                    p2 += 1


            sorted_list += left[p1:]
            sorted_list += right[p2:]

            return sorted_list


        return merge_sort(nums)
        return quickSort(nums)

        
solution = Solution()

nums = [5, 3, 2, 4,6, 10]

print(solution.sortArray(nums))
