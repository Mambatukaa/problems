"""


Roman numerals are represented by seven different symbols: 1, V, X, L, C, D and M.

Symbol Value

I 1
V 5
X 10
L 50
100
D 500
M 1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which
is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not
IIII. Instead, the number four is written as IV . Because the one is before the five we subtract it making four.

The same principle applies to the number nine, which is written as IX. There are six instances where
subtraction is used:
    • I can be placed before V (5) and X (10) to make 4 and 9.
    • X can be placed before L (50) and C (100) to make 40 and 90.
    • C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.



Constraints:
• 1 < s. length <= 15
• s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
• It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


# Time Complexity: O(n) ==> O(1) fixed size
# Space Complexity: O(1)
def romanToInt(s):
    map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    res = 0
    i = 0

    while i < len(s):
        curr = map[s[i]]
        next = map[s[i + 1]] if i + 1 < len(s) else -1

        if curr < next:
            res += next - curr
            i += 1
        else:
            res += curr

        i += 1


    return res

# Optimized for fast look up
def romanToIntII(s):
    map = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }

    res = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in map:
            res += map[s[i: i + 2]]
            i += 1
        else:
            res += map[s[i]]

        i += 1


    return res

s = "XIV"
print("Res:", romanToInt(s))
