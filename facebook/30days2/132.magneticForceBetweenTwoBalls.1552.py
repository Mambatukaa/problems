"""
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

 

Example 1:


Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.
 

Constraints:

n == position.length
2 <= n <= 105
1 <= position[i] <= 109
All integers in position are distinct.
2 <= m <= position.length


Complexity Analysis
Here, n is the number of elements, and k is the maximum position value in the position array.

Time complexity: O(nlog 
m
n∗k
​
 )

Sorting the position array takes O(nlogn) time.

Checking if we can place the balls in the position array takes O(n) time. This operation is repeated until we reduce our search space to one element. The search space is halved in each step until only one element remains, resulting in O(log 
m
k
​
 ) steps.
a→a/2→a/4→...→1 (b steps)
a/2 
(b−1)
 =1⟹b≈loga

Therefore, the overall time complexity is O(nlog 
m
n∗k
​
 ).

Space complexity: O(logn) or O(n)

Apart from sorting, we do not use any additional space.

The space complexity of the sorting algorithm depends on the programming language.

In Python, the sort method sorts a list using the Timsort algorithm which is a combination of Merge Sort and Insertion Sort and has O(n) additional space.
In Java, Arrays.sort() is implemented using a variant of the Quick Sort algorithm which has a space complexity of O(logn) for sorting two arrays.
In C++, the sort() function is implemented as a hybrid of Quick Sort, Heap Sort, and Insertion Sort, with a worse-case space complexity of O(logn).
"""
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        # place with mid distance 
        # if it's possible extend the distance else minimize the distance

        def canPlace(mid):
            prev_ball_pos = position[0]
            balls_placed = 1

            for i in range(1, len(position)):
                curr_pos = position[i]

                if curr_pos - prev_ball_pos >= mid:
                    balls_placed += 1
                    prev_ball_pos = curr_pos

                if balls_placed == m:
                    return True
            return False


        position.sort()

        l = 1
        r = (position[-1] // (m - 1)) + 1

        while l < r:
            mid = (l + (r - l) // 2) + 1

            if canPlace(mid):
                # extend the size
                l = mid
            else:
                # shrink the side
                r = mid - 1
        
        return r
        
        
"""

*           *
1, 2, 3, 4, 7     m = 2

(7 // 1) + 1 = 8

l = 1
r = 8

mid = = 3




22 57 74 79,  m = 4

l = 1
r = (79 // 3) + 1 = 27

mid = 14

"""
