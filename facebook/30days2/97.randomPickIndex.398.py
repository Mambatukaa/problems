


""""
Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.
 

Example 1:

Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
target is an integer from nums.
At most 104 calls will be made to pick.


"""


# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def __init__(self, nums: List[int]):
        self.dic = defaultdict(list)

        for i, num in enumerate(nums):
            self.dic[num].append(i)

    def pick(self, target: int) -> int:

        return random.choice(self.dic[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)



"""
 0 1 2 3 4
[1,2,3,3,3] ,[3],[1],[3]
   null       4,  0,  2


dic = {
    1: [0]
    2: [1]
    3: [2, 3, 4]
}



Reservoir sampling is a technique which is used to generate numbers randomly when we have a large pool of numbers. 
As mentioned in the note for this question, the array size can be large, hence it is a reasonable choice to use Reservoir Sampling. 
Consider an array of size n from which we need to chose a number randomly. 
Consider these numbers to be coming in the form of a stream, hence at each step, we have to take the decision of whether or not to choose a given number, such that the overall probability of each number being chosen is same (

"""
# Reservoir sampling 

# Time Complexity: O(n)
# Space Complexity: O(1)
# TLE
class Solution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target: int) -> int:
        print("----------------------------------------")
        count = 0
        idx = -1
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                # pick current index with probability 1/count
                if random.randint(1, count) == 1:
                    idx = i
        return idx

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)



"""
 0 1 2 3 4
[1,2,3,3,3] ,[3],[1],[3]
   null       4,  0,  2


dic = {
    1: [0]
    2: [1]
    3: [2, 3, 4]
}




"""
