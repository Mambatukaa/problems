/* @param {number} n
// initial
//
///**
 * @param {number[][]} connections
 * @return {number}
 */
// Time Complexity: O(n ^ 2);
// Space Complexity: O(n);
var minReordera = function(n, connections) {
//   // pass curr node = 0;
//   Search node from unvisited connections
//   a. found
//     if current node not in 1th index 
//       swap and increase the counter
//     add item index to the visited
//     call the function with neighbor  
//   b. not found
//     do nothing

  let answer = 0;
  const visited = new Set();

  const dfs = (val) => {
    for(let i = 0; i < n - 1; i++) {
      if(visited.has(i)) {
        continue;
      };

      const currItem = connections[i];
      const firstEl = currItem[0];
      const secondEl = currItem[1];

      if(firstEl === val || secondEl === val) {

        if(firstEl === val) {
          // swap
          [currItem[0], currItem[1]] = [currItem[1], currItem[0]];
          connections[i] = currItem;
          answer++;
        };

        visited.add(i);
        dfs(currItem[0]);
      };
      
    };

  };

  dfs(0)
    
  return answer;
}

// Visiting each node once
// Time Complexity: O(n);
// Space Complexity: O(n);
 var minReorder = function(n, connections) {
  const roads = new Set();
  const graph = new Map();

    // build undirected graph
  for(const [x, y] of connections) {
    if(!graph.has(x)) {
      graph.set(x, []);
    };

    if(!graph.has(y)) {
      graph.set(y, []);
    };

    graph.get(x).push(y);
    graph.get(y).push(x);

    roads.add(`${x},${y}`);
  };

  const seen = new Set();
  seen.add(0);

  const dfs = (node) => {
    const neighbors = graph.get(node);

    let answer = 0;
    for(const neighbor of neighbors) {
      if(!seen.has(neighbor)) {
        if(roads.has(`${node},${neighbor}`)) {
          answer++;
        };

        seen.add(neighbor);
        answer += dfs(neighbor);
      };

    };

    return answer;
  };


 return dfs(0);
};

// Time Complexity: O(n)
// Space Complexity: O(n)
const minReorderIterative = (n, connections) => {

  const convertToHash = (from, to) => {
    return `${from},${to}`;
  };

  // build undirected graph
  const graph = new Map();
  const roads = new Set();

  for(let i = 0; i < n; i++) {
    graph.set(i, []);
  };

  for(const [from, to] of connections) {
    graph.get(from).push(to);
    graph.get(to).push(from);

    roads.add(convertToHash(from, to));
  };

  console.log(graph)

  const visited = new Array(n).fill(false);
  // do the DFS on graph and search (node, neighbor) from roads
  // if found ? increase the answer
  // track visited pair
  
  let answer = 0;
  const stack = [0];
  visited[0] = true;

  while(stack.length) {
    const currNode = stack.pop();
    const neighbors = graph.get(currNode);

    for(const neighbor of neighbors) {
      if(!visited[neighbor]) {
        if(roads.has(convertToHash(currNode, neighbor))) {
          answer++;
        };

        visited[neighbor] = true;
        stack.push(neighbor);
      };
    };
  };


  return answer;
};

const connections = [[0,1],[1,3],[2,3],[4,0],[5,4]];
const n = 6;

console.log(minReorderIterative(n, connections));

/*

n = 5, connections = [[1,0], [1,2], [3,2], [3, 4]];

0 <---- 1 ----> 2 <---- 3 ----> 4
          <----           <----

output: 2;          

Need to change to routes to reach 0.


1. Need to find [0, ?] || [?, 0]

  // pass curr node = 0;
  Search node from unvisited connections
  a. found
    if current node not in 1th index 
      swap and increase the counter
    add item index to the visited
    call the function with neighbor  
  b. not found
    do nothing


Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

      3 <--- 2
     /
    /
   1 
  /
 /
0 <--- 4 ---> 5
         <---   


Find nodes which connected to 0.
  and swap if necessary
    get neighbor node
    Find nodes that connected with neighbor
    if necesseary swap






  0 1 2 3 4 5
0 0 1 0 0 0 0
1 0 0 0 1 0 0
2 0 0 0 1 0 0
3 0 0 0 0 0 0
4 1 0 0 0 0 1
5 0 0 0 0 0 0

0: 1
1: 3
2: 3
3: 
4: 0, 5
5:

visited = new Set();
answer = 0;

pass node of 0

1. Build adjacency List graph (because nodes have least connection)
2. Iterate through unvisited nodes
  a. Pass the node BFS/DFS function.
  b. Iterate through unvisited neighbors of currentNode
      add neighbor to the visited set
      increase the answer
      call bfs on neighbor
3. return answer




Input: n = 6, connections = [[0,1],[3,1],[2,3],[4,0],[5,4]]

   1 <--- 3 <--- 2
  /
 /
0 <--- 4 <--- 5

Directed Graph
0: [1] 
1: []
2: [3]
3: [1]
4: [0]
5: [4]

Undirected Graph
0: [1, 4] 
1: [0, 3]
2: [3]
3: [1, 2]
4: [0, 5]
5: [4]


*/





/*

Input: n = 6, connections = [[0,1],[3,1],[2,3],[4,0],[5,4]]

   1 <--- 3 <--- 2
  /
 /
0 <--- 4 <--- 5

Directed Graph
0: [1] 
1: []
2: [3]
3: [1]
4: [0]
5: [4]

[[0,1],[3,1],[2,3],[4,0],[5,4]]

Undirected Graph
0: [1, 4] 
1: [0, 3]
2: [3]
3: [1, 2]
4: [0, 5]
5: [4]



1. Create Undirected graph. Add connection to the set.
2. Do the DFS on undirected graph. Check (node, neighbor) from set. If found increase the answer

 */
