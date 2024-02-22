/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function(isConnected) {
  // build graph
  const n = isConnected.length;

  const graph = new Map();

  for(let i = 0; i < n; i++) {
    graph.set(i, []);
  };

  for(let i = 0; i < n; i++) {
    for(let j = i + 1; j < n; j++) {
      if(isConnected[i][j] === 1) {
        graph.get(i).push(j);
        graph.get(j).push(i);
      }
    };
  };
  
  const visited = new Set();
  let provinces = 0;

  // Time Complexity: O(E)
  // Space Complexity: O(E)
  const bfs = (vertice) => {
    const queue = [vertice];

    while(queue.length) {
      const currVertice = queue.shift()
      const neighbors = graph.get(currVertice);

      for(const neighbor of neighbors) {
        if(!visited.has(neighbor)) {
          queue.push(neighbor);
          visited.add(neighbor);
        }
      };

    };

  };

  // Time Complexity: O(E)
  // Space Complexity: O(E)
  const dfs = (vertice) => {
    const stack = [vertice];

    while(stack.length) {
      const currVertice = stack.pop()
      const neighbors = graph.get(currVertice);

      for(const neighbor of neighbors) {
        if(!visited.has(neighbor)) {
          stack.push(neighbor);
          visited.add(neighbor);
        }
      };

    };

  };

  // Time Complexity: O(E)
  // Space Complexity: O(E)
  const dfsRecursive = (vertice) => {
    const neighbors = graph.get(vertice);

    for(const neighbor of neighbors) {
      if(!visited.has(neighbor)) {
        visited.add(neighbor);
        dfsRecursive(neighbor);
      };
    };

  };

  // Time Complexity: O(V + E) // For this example building graph takes O(n^2)
  // Space Complexity: O(V + E)
  for(let i = 0; i < n; i++) {
    if(!visited.has(i)) {
      provinces++;
      dfs(i);
    };

  };



  return provinces;
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
