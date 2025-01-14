# String to integer(atoi)


"""

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:
    1. Whitespace: Ignore any leading whitespace (" ").

    2. Signedness: Determine the sign by checking if the next character is "-' or , assuming positivity if
    neither present.

    3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the
    end of the string is reached. If no digits were read, then the result is 0.

    4. Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer
    to remain in the range. Specifically, integers less than -231 should be rounded to -2^31 , and integers greater
    than 2^31 - 1 should be rounded to 2^31 - 1.

Return the integer as the final result.


Constraints:

• 0 < s. length <= 200
• s consists of English letters (lower-case and upper-case), digits (0-9), '+', '-', and ""'.

"""


def myAtoi(self, s: str) -> int:
    # remove leading spaces
    s = s.lstrip()

    if not s:
        return 0
        
    idx = 0
    sign = 1
    res = 0

    # mark the sign
    if s[0] == "-":
        sign = -1
        idx += 1

    if s[0] == "+":
        idx += 1

    # isdigit() is numberic
    for i in range(idx, len(s)):
        ch = s[i]

        if not ch.isdigit():
            break

        res *= 10
        res += int(ch)

    # check the res reached the range or not
    if res > 2**31 - 1:
        res = 2 ** 31

        # check is it positive
        if sign == 1:
            res -= 1


    return res * sign

        


s = "42"

print("res:", myAtoi(s))

s = "1337c0d3"

print("res:", myAtoi(s))
s = "w"

print("res:", myAtoi(s))

"""

"""

