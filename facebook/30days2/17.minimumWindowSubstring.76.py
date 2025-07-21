# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)

        need, have = 0, len(t_count)
        s_count = defaultdict(int)

        res = [0, -1]
        res_len = float('inf')

        l = 0

        for r in range(len(s)):
            curr = s[r]
            s_count[curr] = s_count.get(curr, 0) + 1

            if curr in t_count and t_count[curr] == s_count[curr]:
                need += 1

            while have == need:
                # update the answer and shrink the window
                if res_len > r - l:
                    res = [l, r]
                    res_len = r - l + 1


                if s[l] in t_count and t_count[s[l]] == s_count[s[l]]:
                    need -= 1

                s_count[s[l]] -= 1
                l += 1

        return s[res[0]:res[1] + 1]

"""

RETURN THE MINIMUM SUBSTRING which includes every character in t


s = "ADOBECODEBANC"

t = "ABC"

Follow up: Could you find an algorithm that runs in O(m + n) time?
       

SLIDING WINDOW

1. Slide the window until window becomes valid 
2. If the window is valid update the answer and shrink the window 


How to know the window is valid or not?
    1. counter = 0
    2. Slide the window and if the current character's count == t_count[char]: increase the counter
    3. Shrink the window and if the current character's count < t_count[char]: decrease the counter

    if counter == len(t_counter) window is valid 
    else:
        not valid



return the answer

"""
