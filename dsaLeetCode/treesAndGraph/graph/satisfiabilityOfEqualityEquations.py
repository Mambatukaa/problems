
from collections import defaultdict

def equationsPossible(equations):
  graph = defaultdict(set)


  for _, equation in enumerate(equations):
    

equations = ["b==a", "a!=a"]

print("res:", equationsPossible(equations))

"""

Input: equations = ["a==b", "b!=a"]
Output: False

********************************************************************************

Input: equations = ["a==b", "b==a"]
Output: True


Constraints:
  equations[i][0] and equations[i][3] lowercase english letters
  equations[1] is either '=' or '!'
  equations[2] is '='


Adjacency list


"""
