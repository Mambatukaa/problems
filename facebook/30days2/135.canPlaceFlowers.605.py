"""

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length



"""
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placed = 0

        m = len(flowerbed)
        i = 0

        while i < m:
            empty_left_plot = 0 if i == 0 else flowerbed[i - 1]
            empty_right_plot = 0 if i == m - 1 else flowerbed[i + 1]

            if flowerbed[i] == empty_left_plot == empty_right_plot == 0:
                placed += 1
                i += 2
            elif flowerbed[i]:
                i += 2
            else:
                i += 3
            
            if placed >= n:
                return True

        return False

        
        
"""

[1,1,0,0,0],

"""
