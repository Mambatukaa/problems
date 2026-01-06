""""

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.

 

Example 1:

Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
Example 2:

Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.
 

Constraints:

3 <= arr.length <= 100
0 <= arr[i] <= 1000
0 <= a, b, c <= 1000


"""






class Solution:
    # Enumeration
    # Time Complexity: O(n^3)
    # Space Complexity: O(1)
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:
        n = len(arr)

        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    first = arr[i]
                    second = arr[j]
                    third = arr[k]


                    if abs(first - second) <= a and abs(second - third) <= b and abs(first - third) <= c:
                        res += 1

        
        return res

    # Time Complexity: O(n^2 + nS) S upper limit
    # Space Complexity: O(S)
    def countGoodTripletsII(self, arr, a: int, b: int, c: int) -> int:
        res = 0

        N = len(arr)

        prefix_cnt = [0] * 1001 # prefix_cnt 

        for j in range(N - 1):
            for k in range(j + 1, N):
                if abs(arr[j] - arr[k]) <= b:
                    # how many values before j
                    # where abs conditions met
                    r = min(arr[j] + a, arr[k] + c)
                    l = max(arr[j] - a, arr[j] - c)

                    l = max(l, 0)
                    r = min(r, 1000)

                    if l <= r:
                        res += prefix_cnt[r] - (0 if l == 0 else prefix_cnt[l - 1])

            for index in range(arr[j], 1001):
                prefix_cnt[index] += 1

        return res


solution = Solution()

arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
print("res:", solution.countGoodTripletsII(arr, a, b, c))
