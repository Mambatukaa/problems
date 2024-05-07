# Naive solution
# Time Complexity: O(m * 2^m) m = nums.length
# Space Complexity: O(m * 2^m) m = nums.length
class Solution:
    def subsetsWithDup(self, nums):

        res = []
        seen = {}
        nums.sort()

        def backtracking(curr, start):
            if start > len(nums):
                return


            s = ""
            for num in curr:
                s += str(num)

            if not seen.get(s):
                res.append(curr[:])
            seen[s] = True

            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtracking(curr, i + 1)
                curr.pop()
        
        backtracking([], 0)

        return res

solution = Solution()

print("res:", solution.subsetsWithDup([1,2,2]))
print("************************************************************")

class Solution1:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()

        def backtracking(curr, start):
            if start > len(nums):
                return

            res.append(curr[:])

            for i in range(start, len(nums)):
                if i > start and nums[i - 1] == nums[i]:
                    continue

                curr.append(nums[i])
                backtracking(curr, i + 1)
                curr.pop()

        backtracking([], 0)

        return res

solution = Solution1()

print("res:", solution.subsetsWithDup([1,2,2]))

# Neetcode
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)
class Solution2:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()

        def backtracking(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return
            
            # All subsets that include nums[i]
            subset.append(nums[i])
            backtracking(i + 1, subset)
            subset.pop()

            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtracking(i + 1, subset)

        backtracking(0, [])

        return res

solution = Solution2()

print("res:", solution.subsetsWithDup([1,2,2]))
