""""
You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:

bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.
 

Example 1:

Input: 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
Example 2:

Input: 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output: 
[null,true,true,2,false,-1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
 

Constraints:

2 <= path.length <= 100
1 <= value <= 109
Each path is valid and consists of lowercase English letters and '/'.
At most 104 calls in total will be made to createPath and get.


Data structure like trie

1. split by / /leet/code ----> [leet, code]
2. Iterate through path go 


{
    "leet": { val: 1, children: {

    }
}



"""

from collections import defaultdict
"""

Time Complexity: O(M), where M is the length of path. All the time is actually consumed by the operation that gives us the parent path. We first spend O(M) on finding the last "/" of the path and then another O(M) to obtain the parent string. Searching and addition into a HashMap/dictionary takes an ammortized O(1) time.
Space Complexity: O(K) where K represents the number of unique paths that we add.
"""

class FileSystem:

    def __init__(self):
        self.paths = defaultdict()

    def createPath(self, path: str, value: int) -> bool:
        if path == "/" or len(path) == 0 or path in self.paths:
            return False


        parent = path[:path.rfind('/')]

        if len(parent) > 1 and parent not in self.paths:
            return False

        self.paths[path] = value

        return True

        # return false if path already exists or it's parent doesn't exists
        

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)

        # if path doesn't exist return -1



""""
Complexity Analysis

Before we get into the complexity analysis, let's see why one might prefer the Trie approach. The main advantage of the trie based approach is that we are able to save on space. All the paths sharing common prefixes can be represented by a common branch in the tree. The disadvantage however is that the get operation no longer remains O(1).

Time Complexity:
create ~ It takes O(T) to add a path to the trie if it contains T components.
get ~ It takes O(T) to find a path in the trie if it contains T components.
Space Complexity:
create ~ Lets look at the worst case space complexity. In the worst case, none of the paths will have any common prefixes. We are not considering the ancestors of a larger path here. In such a case, each unique path will end up taking a different branch in the trie. Also, for a path containing T components, there will be T nodes in the trie.
get ~ O(1).





"""

class TrieNode:
    def __init__(self):
        self.map = defaultdict(TrieNode)
        self.value = -1

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        components = path.split("/")[1:]

        cur = self.root

        for i, component in enumerate(components):
            if component not in cur.map:
                if i == len(components) - 1:
                    cur.map[component] = TrieNode()
                else:
                    return False
            
            cur = cur.map[component]

        if cur.value != -1:
            return False

        cur.value = value

        return True


    def get(self, path: str) -> int:

        components = path.split("/")[1]

        cur = self.root

        for component in components:
            if component not in cur.map:
                return False

            cur = cur.map[component]


        return cur.value

                




fileSystem = FileSystem()

print(fileSystem.createPath("/a", 1))
print(fileSystem.get("/a"))

        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)



