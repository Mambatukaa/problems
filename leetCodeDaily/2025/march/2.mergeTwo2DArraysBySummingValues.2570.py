""""


You are given two 2D integer arrays nums1 and nums2.
• nums1 [i] = [idi, valil indicate that the number with the id idi has a value equal to vali•
• nums2 [i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.

Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:
• Only ids that appear in at least one of the two arrays should be included in the resulting array.
• Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in
one of the two arrays, then assume its value in that array to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.

Example 1:
    Input: nums1 = [[1,2], [2,31, [4,5]], nums2 = [[1,4], [3,2], [4,1]]
    Output: [[1,6], [2,3], [3,2], [4,6]]
    Explanation: The resulting array contains the following:
    - id = 1, the value of this id is 2 + 4 = 6.
    - id = 2, the value of this id is 3.
    - id = 3, the value of this id is 2.
    - id = 4, the value of this id is 5 + 1 = 6.

Example 2:
    Input: nums1 = [[2,4], [3,6], [5,5]], nums2 = [[1,3], [4,3]]|
    Output: [[1,3], [2,4], [3,6], [4,3], [5,5]]|
    Explanation: There are no common ids, so we just include each id with its value in the resulting list.


Constraints:
    • 1 <= nums1. length, nums2. length <= 200
    • nums1 [i]. length == nums2 [j]. length == 2
    • 1 < idi, vali <= 1000
    • Both arrays contain unique ids.
    • Both arrays are in strictly ascending order by id.
"""

class Solution:
    # Time Complexity: O(n + m)
    # Space Complexity: O(1)
    def mergeArrays(self, nums1, nums2):
        res = [0] * 1001

        for idx, num in nums1:
            res[idx] += num

        for idx, num in nums2:
            res[idx] += num


        ans = []

        for i in range(len(res)):
            if res[i] != 0:
                ans.append([i, res[i]])

        return ans


    # 2 pointers
    # Time Complexity: O(n + m)
    # Space Complexity: O(n + m)
    def mergeArraysII(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)

        ptr1 = ptr2 = 0

        mergedArray = []

        while ptr1 < n and ptr2 < m:
            idx1 = nums1[ptr1][0]
            idx2 = nums2[ptr2][0]

            value1 = nums1[ptr1][1]
            value2 = nums2[ptr2][1]
            
            if idx1 == idx2:
                mergedArray.append([idx1, value1 + value2])
                ptr1 += 1
                ptr2 += 1

            elif idx1 < idx2:
                mergedArray.append([idx1, value1])
                ptr1 += 1
            else:
                mergedArray.append([idx2, value2])
                ptr2 += 1
                

        while ptr1 < n:
            mergedArray.append([nums1[ptr1][0], nums1[ptr1][1]])
            ptr1 += 1

        while ptr2 < m:
            mergedArray.append([nums2[ptr2][0], nums2[ptr2][1]])
            ptr2 += 1



        return mergedArray
