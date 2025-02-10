""""



You are given a O-indexed array of positive integers w where w[i] describes the weight of the ith index.
You need to implement the function pickIndex), which randomly picks an index in the range range w. length - 11 (inclusive) and returns it. The
probability of picking an index i is w[il / sum(w) .
• For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 +
3) = 0.75 (i.e., 75% ).

Example 1:
    Input
    ["Solution","pickIndex"]
    Output
    [null,0]
    Explanation
    Solution solution = new Solution ( [1]);
    solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in W.

Example 2:
    Input
    "Solution" ',"pickIndex","pickIndex","pickIndex". ,"pickIndex" ',"pickIndex"]
    [ [ [1, 3]1, [1, [1, [], [], [1]
    Output
    [null,1,1,1,1,0]


Constraints:
• 1 <= w. length <= 104
• 1 < w[i] <= 105
• pickIndex will be called at most 104 times.


"""


import random
class Solution:

    # Prefix_sum
    # Time Comlexity: O(n)
    # Space Comlexity: O(n)
    def __init__(self, w):
        self.prefix_sums = []
        prefix_sum = 0

        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    # Time Comlexity: O(n)
    # Linear search
    def pickIndex(self) -> int:
        target = self.total_sum * random.random()

        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i

    # Time Comlexity: O(log n)
    # Binary search
    def pickIndexII(self) -> int:
        target = self.total_sum * random.random()
        print(target)
        l = 0
        r = len(self.prefix_sums)

        while l < r:
            mid = l + (r - l) // 2

            if target > self.prefix_sums[mid]:
                l = mid + 1
            else:
                r = mid

        return l



w = [1, 2, 3, 4]
w = [1, 2, 1000]
solution = Solution(w)
print("res 1:", solution.pickIndex())
print("res 2:", solution.pickIndexII())

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
#
#
# 1 , 3 ===> 2
# 1 + 3 == 4 / 2 == 2
# 3 //2 + 1 = 2
# 1 + 5 = 6 / 2 = 
# 10 + 20 = 30 / 2 = 15
# (20 - 10) / 2 + 10 = 15
#
# r - l / 2 + l =
