""""



You are given an absolute path for a Unix-style file system, which always begins with a slash */'. Your task is to transform this absolute path
into its simplified canonical path.

The rules of a Unix-style file system are as follows:
    • A single period '.' represents the current directory.
    • A double period '..' represents the previous/parent directory.
    • Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/' .
    • Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, ' ...'
    and '....' are valid directory or file names.

The simplified canonical path should follow these rules:
    • The path must start with a single slash '/'.
    • Directories within the path must be separated by exactly one slash '/'.
    • The path must not end with a slash '/', unless it is the root directory.
    • The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.



Example 1:
    Input: path = "/home/"
    Output: "/home"
Explanation:
    The trailing slash should be removed.


Example 2:
    Input: path = "/home//foo/"
    Output: "/home/foo"
Explanation:
    Multiple consecutive slashes are replaced by a single one.



Constraints:
• 1 <= path. length <= 3000
• path consists of English letters, digits, period "', slash "/' or *'
• path is a valid absolute Unix path.

"""



class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""

        for ch in path + "/":
            if ch != "/":
                curr += ch
            else:
                if curr == "..":
                    if stack:
                        stack.pop()
                elif curr and curr != ".":
                    stack.append(curr)
                curr = ""

        return "/" + "/".join(stack)


solution = Solution()

path = "//.../a//../b/c/../d/./aa"
path = "/a/../c/"
path = "/abc//../aa"
path = "/../"




print("res:", solution.simplifyPath(path))
