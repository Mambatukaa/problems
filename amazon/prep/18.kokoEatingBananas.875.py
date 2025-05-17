""""




Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109











"""











class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)

        while lower <= upper:
            mid = lower + (upper - lower) // 2
            hour = 0

            # try to finish with mid speed
            for pile in piles:
                hour += math.ceil(pile / mid)

            # if spending more time eat fast
            if hour > h:
                lower = mid + 1
            # else spending less time eat slow
            else:
                upper = mid - 1

        return lower





       # Likes to eat slowly but still wants to finish eating all bananas 
       # Brute force
       # Starts to eat maximum speed
       # If it's possible reduce the speed
       # Reduce the speed until it's not possible
       # The min speed which was possible is the result
       # piles = [3, 6, 7, 11] h = 8
       # starts to eat 11 and check is it possible to eat in 8 hours
        # if it's possible -1
        # else return minTime
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)

       # Optimized binary search
        # Time Complexity: O(log n * n)








