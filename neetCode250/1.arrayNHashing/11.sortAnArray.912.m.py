""""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""


# TC: O(n log n) worst O(n^2)
# SC: O(n) worst O(n^2)
# Quick sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def quickSort(nums):
            if not nums:
                return []
            pivot = random.choice(nums)
            left = []
            mid = []
            right = []

            for num in nums:
                if num < pivot:
                    left.append(num)
                elif num > pivot:
                    right.append(num)   
                else:
                    mid.append(num)
            
            return quickSort(left) + mid + quickSort(right)
        
        return quickSort(nums)




# Counting sort
# TC: O(n + k)
# SC: O(n)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_value = min(nums)
        max_value = max(nums)

        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        res = []

        for num in range(min_value, max_value + 1, 1):
            if num in counter:
                res += [num] * counter[num]

                del counter[num]
            
        
        return res





""""

Complexity Analysis
Here, n is the number of elements in the nums array, d is the maximum number of digits and b is the size of the bucket used.

Time complexity: O(d⋅(n+b))

We iterate on the array elements to find the maximum number and then find the count of its digits, thus taking O(n+d) time.
Then we sort the array for each integer place which will take O(n+b) time, thus for all d places it will take O(d⋅(n+b)) time.
At the end, we seperate out positive and negative numbers and reverse the negatives, which overall will take O(n) time.
Thus, overall it takes O((n+d)+d⋅(n+b)+n)=O(d⋅(n+b)) time.
Space complexity: O(n+b)

We use additional arrays negatives and positives which use O(n) space and buckets which use O(n+b) space.

"""
class Solution:
    # Radix sort function.
    def radix_sort(self, nums: List[int]) -> List[int]:
        # Find the absolute maximum element to find max number of digits.
        max_element = nums[0]
        for val in nums:
            max_element = max(abs(val), max_element)

        max_digits = 0
        while max_element > 0:
            max_digits += 1
            max_element = max_element // 10

        place_value = 1
        
        # Bucket sort function for each place value digit.
        def bucket_sort():
            buckets = [[] for i in range(10)]
            # Store the respective number based on it's digit.
            for val in nums:
                digit = abs(val) / place_value
                digit = int(digit % 10)
                print(val, "digit:", digit)
                buckets[digit].append(val)
            print(buckets)

            # Overwrite 'nums' in sorted order of current place digits.
            index = 0
            for digit in range(10):
                for val in buckets[digit]:
                    nums[index] = val
                    index += 1
            
            print("nums:", nums)

        # Radix sort, least significant digit place to most significant.      
        for _ in range(max_digits):
            print('-----------------------', place_value)
            bucket_sort()
            place_value *= 10

        print(nums)
        # Seperate out negatives and reverse them. 
        positives = [val for val in nums if val >= 0]
        negatives = [val for val in nums if val < 0]
        negatives.reverse()

        # Final 'arr' will be 'negative' elements, then 'positive' elements.
        return negatives + positives
            
    def sortArray(self, nums: List[int]) -> List[int]:  
        return self.radix_sort(nums)                                                      