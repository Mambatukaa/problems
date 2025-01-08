
"""

Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.
A substring is a contiguous sequence of characters within a string

Example 1:
    Input: words = ["mass", "as", "hero", "superhero"]
    Output: ["as", "hero"]

    Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".



"""


# Naive approach
# Brute force
# Time Complexity: O(n^2 * m^2)
# Space Complexity: O(n * m)
def stringMatching(words):
    res = []

    for currWord in words:

        for otherWord in words:
            if currWord == otherWord:
                continue

            if currWord in otherWord:
                res.append(currWord)
                break

    return res



words = ["mass", "as", "hero", "superhero"]


print("res:", stringMatching(words))
