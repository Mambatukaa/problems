""""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
 

Constraints:

1 <= n <= 231 - 1
1 <= pick <= n


"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# TC: O(log N)
# SC: O(1)
class Solution:
    def guessNumber(self, n: int) -> int:

        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2

            if guess(mid) == 0:
                return mid
            
            if guess(mid) == 1:
                low = mid + 1
            else:
                high = mid - 1
        return -1


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# TC: O(log,3 N)
# SC: O(1)
class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid1 = low + (high - low) // 3
            mid2 = high - (high - low) // 3
            res1 = guess(mid1)
            res2 = guess(mid2)

            if res1 == 0:
                return mid1
            if res2 == 0:
                return mid2
            elif res1 < 0:
                high = mid1 - 1
            elif res2 > 0:
                low = mid2 + 1
            else:
                low = mid1 + 1
                high = mid2 - 1
        return -1

        
