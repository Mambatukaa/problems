"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109


"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        nums=list(map(str,nums))
        def compare(x,y):

            if x+y>y+x:
                return -1

            elif y+x>x+y:
                return 1

            else:
                return 0
        nums.sort(key=cmp_to_key(compare))

        if nums[0]=="0":

            return "0"

        return ''.join(nums)


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Edge case: if all numbers are zero, return "0"
        if not any(nums):
            return "0"

        # Custom comparison function for heapq (simulating the comparator in Java)
        class LargerStrComparator(str):
            def __lt__(self, other):
                # Custom comparison: return True if self+other > other+self
                return self + other > other + self

        # Priority queue (min-heap), but we push elements using a custom comparator
        heap = []
        for num in nums:
            heapq.heappush(heap, LargerStrComparator(str(num)))

        # Build the result string by popping from the heap
        result = []
        while heap:
            result.append(heapq.heappop(heap))

        # Concatenate and return the result
        largest_num = "".join(result)

        # Handle case where all elements are "0"
        return "0" if largest_num[0] == "0" else largest_num

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert each integer to a string
        num_strings = [str(num) for num in nums]

        # Sort strings based on concatenated values
        num_strings.sort(key=lambda a: a * 10, reverse=True)

        # Handle the case where the largest number is zero
        if num_strings[0] == "0":
            return "0"

        # Concatenate sorted strings to form the largest number
        return "".join(num_strings)
