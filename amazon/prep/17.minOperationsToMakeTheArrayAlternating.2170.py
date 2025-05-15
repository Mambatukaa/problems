""""
You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:

nums[i - 2] == nums[i], where 2 <= i <= n - 1.
nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.

Return the minimum number of operations required to make the array alternating.

 

Example 1:

Input: nums = [3,1,3,2,4,3]
Output: 3
Explanation:
One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations. 
Example 2:

Input: nums = [1,2,2,2,2]
Output: 2
Explanation:
One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105










"""


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def minimumOperations(self, nums) -> int:
        n = len(nums)

        odd = {}
        even = {}

        for i in range(len(nums)):
            if i % 2:
                # odd
                odd[nums[i]] =odd.get(nums[i], 0) + 1
            else:
                # even
                even[nums[i]] = even.get(nums[i], 0) + 1

        odd_first, odd_second = (None, 0), (None, 0)

        for k, v in odd.items():
            if odd_first[1] < v:
                odd_first, odd_second = (k, v), odd_first
            elif odd_second[1] < v:
                odd_second = (k, v)

        even_first, even_second = (None, 0), (None, 0)

        for k, v in even.items():
            if even_first[1] < v:
                even_first, even_second = (k, v), even_first
            elif even_second[1] < v:
                even_second = (k, v)

        if odd_first[0] != even_first[0]:
            return n - odd_first[1] - even_first[1] 
        else:
            return n - max(odd_first[1] + even_second[1], even_first[1] + odd_second[1])

    # sorting
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    def minimumOperationsII(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return 0

        odd = {}
        even = {}

        for i in range(len(nums)):
            if i % 2:
                # odd
                odd[nums[i]] =odd.get(nums[i], 0) + 1
            else:
                # even
                even[nums[i]] = even.get(nums[i], 0) + 1



        sorted_odd = sorted(odd.items(), key= lambda x: x[1])
        sorted_even = sorted(even.items(), key= lambda x: x[1])

        odd_first, odd_second = sorted_odd[-1], sorted_odd[-2] if len(sorted_odd) > 1 else (None, 0)
        even_first, even_second = sorted_even[-1], sorted_even[-2] if len(sorted_even) > 1 else (None, 0)


        if odd_first[0] != even_first[0]:
            return n - odd_first[1] - even_first[1] 
        else:
            return n - max(odd_first[1] + even_second[1], even_first[1] + odd_second[1])


solution = Solution()
nums = [1,2,2,2,2]
nums = [3,1,3,2,4,3]

print("res:", solution.minimumOperationsII(nums))
