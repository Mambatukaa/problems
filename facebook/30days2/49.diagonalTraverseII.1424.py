""""
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

 

Example 1:


Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
Example 2:


Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i].length <= 105
1 <= sum(nums[i].length) <= 105
1 <= nums[i][j] <= 105
"""


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dic = defaultdict(list)

        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                diagonal = row + col

                dic[diagonal].append(nums[row][col])

        res = []
        curr = 0

        while curr in dic:
            res.extend(dic[curr])
            curr += 1

        return res


# BFS 
class Solution:
    # TIme Complexity: O(n)
    # Space Complexity: O(/n) max size will be the largest diagonal
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # rotate 45 degrees
        # BFS

        q = deque([[0, 0]])

        res = []

        # if col == 0 add bottom
        # to skip duplication

        while q:
            row, col = q.popleft()
            res.append(nums[row][col])

            if col == 0 and row + 1 < len(nums):
                q.append([row + 1, col])

            if col + 1 < len(nums[row]):
                q.append([row, col + 1])

        return res



        
