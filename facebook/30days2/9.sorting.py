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
                if num > pivot:
                    right.append(num)
                elif num < pivot:
                    left.append(num)
                else:
                    mid.append(num)
                    
            return quickSort(left) + mid + quickSort(right)
        
        # Time complexity: O(n log n)
        # Space complexity: O(n)
        def merge_sort(arr):
            # Base case: if the list has 0 or 1 element, it's already sorted
            if len(arr) <= 1:
                return arr
        
            # Divide the list into two halves
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
        
            # Recursively sort the two halves
            sorted_left = merge_sort(left_half)
            sorted_right = merge_sort(right_half)
        
            # Merge the sorted halves
            return merge(sorted_left, sorted_right)
        
        def merge(left, right):
            sorted_nums = []

            l = 0
            r = 0

            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    sorted_nums.append(left[l])
                    l += 1
                else:
                    sorted_nums.append(right[r])
                    r += 1
            
            sorted_nums += left[l:]
            sorted_nums += right[r:]

            return sorted_nums

        return merge_sort(nums)

        