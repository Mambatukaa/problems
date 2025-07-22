""""

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

Example 1:


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
 

Constraints:

0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109 
endj < startj+1

"""
# Time Complexity: O(n + m)
# Space Complexity: O(n + m) response
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []



        p1 = 0
        p2 = 0

        res = []

        while p1 < len(firstList) and p2 < len(secondList):
            first_interval = firstList[p1]
            second_interval = secondList[p2]

            if ((second_interval[0] >= first_interval[0] and second_interval[0] <= first_interval[1]) or 

                (first_interval[0] >= second_interval[0] and first_interval[0] <= second_interval[1]) or

                (first_interval[1] == second_interval[0]) or (second_interval[1] == first_interval[0])

                ):
                    res.append(
        [max(first_interval[0], second_interval[0]), min(first_interval[1], second_interval[1])])

            
            if first_interval[1] > second_interval[1]:
                p2 += 1
            elif first_interval[1] < second_interval[1]:
                p1 += 1
            else:
                p2 += 1
                p1 += 1
    

        return res



class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []



        p1 = 0
        p2 = 0

        res = []

        while p1 < len(firstList) and p2 < len(secondList):
            first_interval = firstList[p1]
            second_interval = secondList[p2]

            begin = max(first_interval[0], second_interval[0])
            end = min(first_interval[1], second_interval[1])

            # intersection exists
            if begin <= end:
                res.append([begin, end])
            
            if first_interval[1] > second_interval[1]:
                p2 += 1
            else:
                p1 += 1
    

        return res



"""

Are intervals sorted?

If not sort the intervals


** One interval can be more than 1 intersections

2 pointers

compare two intervals at a time.

check is there any intervals?
    if (second_interval[0] >= first_interval[0] and second_interval[0] <= first_interval[1]) or 
       (first_interval[0] <= second_interval[0] and first_interval[0] <= second_interval[1]):

       # intersection








"""
