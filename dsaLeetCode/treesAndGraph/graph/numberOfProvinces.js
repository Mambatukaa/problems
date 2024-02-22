/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function(isConnected) {
  const visited = new Set();
  let answer = 0;

 // Space Complexity: O(E)
 // Time Complexity: O(E)
  const dfs = (i) => {
    const stack = [i];

    while(stack.length) {
      const currIdx = stack.pop();
      const neighbors = isConnected[currIdx];

      neighbors.forEach((neighbor, neighborIdx) => {
        if(currIdx !== neighborIdx) {

        // if neighbor is not visited
        if(!visited.has(neighborIdx) && neighbor === 1) {
          stack.push(neighborIdx);
          visited.add(neighborIdx);
        };

      }

      })

      
  
    };
  };

 // Space Complexity: O(E)
 // Time Complexity: O(E)
  const bfs = (i) => {
    const queue = [i];

    while(queue.length) {
      const currIdx = queue.shift();
      const neighbors = isConnected[currIdx];

      neighbors.forEach((neighbor, neighborIdx) => {
        if(currIdx !== neighborIdx) {

        // if neighbor is not visited
        if(!visited.has(neighborIdx) && neighbor === 1) {
          queue.push(neighborIdx);
          visited.add(neighborIdx);
        };

      }

      })
    };
  };

  // Time Complexity: O(V * E)
  // Space Complexity: O(V * E)
  for(let i = 0; i < isConnected.length; i++) {
    if(!visited.has(i)) {
      answer++;
      dfs(i);
      //bfs(i);
    };
  };
    

  return answer;
};




/*
  A B C
A 1 1 0
B 1 1 0
C 0 0 1

A: B
B: A
C: 

Find how many different provinces we have.....

***********  adjacencyMatrix  *********** 
isConnected = [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1]
];

Do BFS || DFS
1. Start from any nodes. 
2. Mark visited nodes.
3. 

. Repeat the search
  a. If found the unvisited node increase the answer;


1 -------- 2

      3


A province is a group of directly or indirectly connected cities and no other cities outside of the group.


*/
