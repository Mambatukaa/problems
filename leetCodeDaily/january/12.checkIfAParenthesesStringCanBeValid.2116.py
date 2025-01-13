"""
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following
conditions is true:
    • It is () .
    • It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
    • It can be written as (A), where A is a valid parentheses string.

You are given a parentheses strings and a string Locked, both of length in. Locked is a binary string consistin
only of '0' s and '1' s. For each index i of locked,
    • If locked [11 is "1', you cannot change s [i] .
    • But if locked is is you you can change stil to either "(' or ")".
Return true if you can make s a valid parentheses string. Otherwise, return false.


"())()))()(()(((())"
"101110110001000100"

"""

# Time Complexity: O(n)
# Space Complexity: O(n)
# Two stacks
def canBeValid(s, locked):
    # edge case 
    if len(s) % 2 == 1:
        return False

    opening = []
    unlocked = []

    for i in range(len(s)):
        if locked[i] == "0":
            unlocked.append(i)
        elif s[i] == "(":
            opening.append(i)
        else:
            if opening:
                opening.pop()
            elif unlocked:
                unlocked.pop()
            else:
                return False

    # match remaining opening and closing brackets

    while opening and unlocked and opening[-1] < unlocked[-1]:
        opening.pop()
        unlocked.pop()

    if opening:
        return False

    return True



s = "(())"
locked = "0111"

print("res:", canBeValid(s, locked))

