""""
You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.

 

Example 1:

    Input: ranks = [4,2,3,1], cars = 10
    Output: 16
    Explanation: 
    - The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
    - The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
    - The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
    - The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
    It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​

Example 2:

    Input: ranks = [5,1,8], cars = 6
    Output: 16
    Explanation: 
    - The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
    - The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
    - The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
    It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
    

Constraints:
1 <= ranks.length <= 10^5
1 <= ranks[i] <= 100
1 <= cars <= 10^6
"""

import math
class Solution:
    # Time Complexity: O(n log m)
    # Space Complexity: O(k)
    def repairCars(self, ranks, cars: int) -> int:
        min_time = 1
        max_time = min(ranks) * cars * cars

        freq = [0] * (max(ranks) + 1)

        for rank in ranks:
            freq[rank] += 1

        while min_time < max_time:
            mid_time = min_time + (max_time - min_time) // 2
            fixed_cars = 0

            # calculate how many cars in mid_time
            for rank in range(1, len(freq)):
                fixed_cars += freq[rank] * int(math.sqrt(mid_time // rank))

            if fixed_cars < cars:
                min_time = mid_time + 1
            else:
                max_time = mid_time

        return min_time



    # Binary search 
    # Time Complexity: O(n*mlog)
    # Space Complexity: O(1)
    def repairCarsII(self, ranks, cars: int) -> int:
        min_time = 1
        max_time = min(ranks) * cars * cars

        while min_time < max_time:
            mid_time = min_time + (max_time - min_time) // 2
            fixed_cars = 0

            # calculate how many cars in mid_time
            for rank in ranks:
                fixed_cars += int(math.sqrt(mid_time // rank))

            if fixed_cars < cars:
                min_time = mid_time + 1
            else:
                max_time = mid_time

        return min_time


solution = Solution()

ranks = [4,2,3,1]
cars = 10

ranks = [1,1,3,3]
cars = 10

"""
1 => 1 * 3 * 3
2 => 2 * 2 * 2
3 => 3 * 1 * 1

"""
print("res:", solution.repairCars(ranks, cars))
print("res:", solution.repairCarsII(ranks, cars))



