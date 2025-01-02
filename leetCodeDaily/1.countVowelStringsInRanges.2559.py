# Range sum problem
# Time Complexity: O(n + m)
# Space Complexity: O(1)
def vowelStrings(words, queries):
    vowelSet = set("aeiou")

    count = [0] * (len(words) + 1)
    prev = 0

    prev = 0
    for i, word in enumerate(words):
        # check the word is valid or not
        if word[0] in vowelSet and word[-1] in vowelSet :
            # valid
            prev += 1

        count[i + 1] = prev

    res = [0] * len(queries)

    for i, q in enumerate(queries):
        l, r = q
        res[i] = count[r + 1] - count[l]


    return res


#       [  0,     1,     2,    3,    4]
#       [  1,     0,     2,    3,    4]
words = ["aba", "bcb", "ece", "aa", "e"]
queries = [ [0,2], [1,4], [1,1]]

print("res:", vowelStrings(words, queries))

"""

You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries [1] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries. length, where ans [11 is the answer to the fith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.


Check how many valid words in queries given range.


Example 1:

Input: words = ["aba", "bcb", "ece", "aa", "e"], queries = [ [0,2], [1,4], [1,1]]

Output: [2,3,0]

Explanation: The strings starting and ending with a vowel are "aba", "ece" "aa" and "e".

    The answer to the query [0,2] is 2 (strings "aba" and "ece") .
    to query [1,4] is 3 (strings "ece", "aa", "e").
    to query [1,1] is 0.
    We return [2,3,0]





    1. Create vowels
    2. Mark valid words
       a. Count the total validWords on each idx
       # Formula = count[r + 1] - count[l]
    3. Check the queries


Input: words = ["aba", "bcb", "ece", "aa", "e"], queries = [ [0,2], [1,4], [1,1]]

Formula = li + ri - (l[i-1] or 0)


 0  1  2  3  4
[1, 1, 2, 3, 4]

"""

