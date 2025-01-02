
"""

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Example 1:
Input: s = "011101"
Output: 5
Explanation:
All possible ways of splitting s into two non-empty substrings are:
    left = "0" and right = "11101", score = 1 + 4 = 5
    left = "01" and right = "1101", score = 1 + 3 = 4
    left = "011" and right = "101", score = 1 + 2 = 3
    left = "0111" and right = "01", score = 1 + 1 = 2
    left = "01110" and right = "1", score = 2 + 1 = 3


Left partitions 0's count + Right partitions 1's count;

countTotalOnes = 4

 p
"011101"

1   4
0 11101

1   3
01 1101


"""

# Time Complexity: O(n)
# Space Complexity: O(1)
def maxScore(s):
    onesCount = 0
    zeroesCount = 1 if s[0] == '0' else 0

    s = s[1:]

    for ch in s:
        if (ch == "1"):
            onesCount += 1

    res = onesCount

    # split the string
    for ch in s:
        print(onesCount, zeroesCount)
        res = max(res, onesCount + zeroesCount)

        if ch == "0":
            zeroesCount += 1
        else:
            onesCount -= 1

    return res

print("res:", maxScore("1111"))
