"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.


"""

# Time Complexity: O(n log n)
# Space Complexity: O(n)
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        sorted_by_value = sorted(count.items(), key=lambda x:x[1], reverse=True)
        res = []

        for k, v in sorted_by_value:
            res.append(k * v)


        return "".join(res)




# Time Complexity: O(n)
# Space Complexity: O(n)
# Bucket sorting
class Solution:
    def frequencySort(self, s: str) -> str:
        # bucket sort
        count = Counter(s)
        max_freq = max(count.values())

        buckets = [[] for _ in range(max_freq + 1)]

        for k, v in count.items():
            buckets[v].append(k)

        res = ""

        for i in range(len(buckets) - 1, 0, -1):
            bucket = buckets[i]

            for letter in bucket:
                res += letter * i
        return res




"""

"treeeeeess"

[], [t, r], [], [], [], [s], [e]

e: 6
s: 2
t: 1
r: 1

max_freq = 2

[[], [], []]

"""


        
