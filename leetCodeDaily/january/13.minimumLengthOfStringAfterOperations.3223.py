"""

You are given a string s.

You can perform the following process on s any number of times:
    • Choose an index i in the string such that there is at least one character to the left of index i that is equal
        to s [il, and at least one character to the right that is also equal to s [il.
    • Delete the closest character to the left of index i that is equal to s [i].
    • Delete the closest character to the right of index i that is equal to s [i].

Return the minimum length of the final string s that you can achieve.

"""

# Time Complexity: O(n) n - is the s length
# Space Complexity: O(1)
def minimumLength(s: str) -> int:
    count = [0] * 26

    for ch in s:
        count[ord(ch) - ord("a")] += 1

    for i in range(len(count)):
        while count[i] > 2:
            count[i] -= 2

    return sum(count)


s = "abaacbcbb"
print("res:", minimumLength(s))

