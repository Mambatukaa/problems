"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""

# TC: O(N log k)
# SC: O(k)
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        max_heap = [(-value, key) for key, value in count.items()]

        heapify(max_heap)

        res = ""

        while max_heap:
            first_val, first_key = heappop(max_heap)

            if not res or res[-1] != first_key:
                res += first_key

                if first_val < -1:
                    heappush(max_heap, (first_val + 1, first_key))
            else:
                # not possible
                if not max_heap:
                    return ""

                second_val, second_key = heappop(max_heap)

                res += second_key

                if second_val < -1:
                    heappush(max_heap, (second_val + 1, second_key))

                # put back unused element
                heappush(max_heap, (first_val, first_key))

        return res
