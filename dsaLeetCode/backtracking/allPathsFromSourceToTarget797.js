/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
// Time Complexity: O(2^n * n)
// Space Complexity: O(n)
var allPathsSourceTarget = function(graph) {
  const answer = [];
  const n = graph.length;

  const backtracking = (idx, curr) => {
    if(idx === n - 1) {
      answer.push([...curr]);
      return;
    };

    const neighbors = graph[idx];

    for(const neighbor of neighbors) {
      curr.push(neighbor);
      backtracking(neighbor, curr);
      curr.pop();
    };
  };

  backtracking(0, [0]);

  return answer;

};


/*

ALL PATHS FROM SOURCE TO TARGET

node 0 to node n - 1..... ALL PATHS.

Input: graph = [[1,2], [3], [3], []]
Output: [[0,1,3], [0,2,3]]
Explanation: There are two paths: 0 → 1 → 3 and 0 → 2 → 3.t



ACYCLIC GRAPH
0: 1 2
1: 3
2: 3
3: 

N 0 1 2 3 
0 0 1 1 0
1 0 0 0 1
2 0 0 0 1
3 0 0 0 0


n = 4;

0 to n - 1 ===== 0 ---> 3


1. Start from 0's neighbors and do DFS until reach the ending point.
2. Track visited nodes and add nodes when reach the ending point.
3. 


*/
