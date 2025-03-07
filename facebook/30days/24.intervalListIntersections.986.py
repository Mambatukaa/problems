""""

You are given two lists of closed intervals, firstList and secondList, where firstList[il = [starti, endil
and secondList[jl = [startj, endjl. Each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
A closed interval [a, bl (with a < b) denotes the set of real numbers & with a = X « b.
the Intersection or [1, 31 and [2, 41 IS [2, 31.
interval. For exampl two closed intervals is a set of real numbers that are either empty or represented as a closed


Example 1 :
    Input: firstList = [[0,21, [5,10],[13,23],[24,25]], secondList = [[1,51, [8,12],
    [15,241, [25,261]
    Output: [[1,2], [5,51, [8,101, [15,23], [24,24], [25,25]]

Example 2:
    Input: firstList = [[1,31, [5,9]], secondList = []
    Output: []

Constraints:
• 0 = firstList.length, secondList.length <= 1000
• firstList.length + secondList.length >= 1
• O < starti < endi <= 109
• endi < starti+1
• O < startj < endj <= 109
• endj < startj+1

"""

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(k)
    # 2 pointers
    def intervalIntersection(self, firstList, secondList):
        n = len(firstList)
        m = len(secondList)

        if not n or not m:
            return []

        res = []

        p1 = 0
        p2 = 0

        while p1 < n and p2 < m:
            first = firstList[p1]
            second = secondList[p2]

            intFirst = max(first[0], second[0])
            intSecond = min(first[1], second[1])


            if intFirst <= intSecond:
                res.append([intFirst, intSecond])

            if first[1] > second[1]:
                p2 += 1
            elif first[1] < second[1]:
                p1 += 1
            else:
                p1 += 1
                p2 += 1


        return res
    

solution = Solution()

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

print("Res:", solution.intervalIntersection(firstList, secondList))
