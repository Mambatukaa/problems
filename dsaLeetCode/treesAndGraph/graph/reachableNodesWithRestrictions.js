/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} restricted
 * @return {number}
 */
// Time Complexity: O(n) // this problem has n nodes and n - 1 edges
// Space Complexity: O(n) // Stack
var reachableNodesII = function(n, edges, restricted) {

  // adjacency list
  const graph = new Map();
  const restrict = new Set(restricted);

  for(let i = 0; i < n; i++) {
    if(restrict.has(i)) {
      continue;
    };

    graph.set(i, []);
  };

  for(const [from, to] of edges) {
    if(restrict.has(from) || restrict.has(to)) {
      continue;
    };

    graph.get(from).push(to)
    graph.get(to).push(from);
  };


  const stack = [0];    
  const seen = new Set();
  seen.add(0);
  let answer = 1;

  while(stack.length) {
    const currNode = stack.pop();
    const neighbors = graph.get(currNode);

    for(const neighbor of neighbors) {
      if(!seen.has(neighbor)) {
        seen.add(neighbor);
        answer++;
        stack.push(neighbor);
      };
    };

  };

  return answer;
};

// Time Complexity: O(n) // this problem has n nodes and n - 1 edges
// Space Complexity: O(n) // Recursive stack
var reachableNodes = function(n, edges, restricted) {

  // adjacency list
  const graph = new Map();
  const restrict = new Set(restricted);

  for(let i = 0; i < n; i++) {
    if(restrict.has(i)) {
      continue;
    };

    graph.set(i, []);
  };

  for(const [from, to] of edges) {
    if(restrict.has(from) || restrict.has(to)) {
      continue;
    };

    graph.get(from).push(to)
    graph.get(to).push(from);
  };


  const seen = new Set();
  seen.add(0);

  const dfs = (node) => {
    const neighbors = graph.get(node);

    let answer = 1;
    for(const neighbor of neighbors) {
      if(!seen.has(neighbor)) {
        seen.add(neighbor);
        answer += dfs(neighbor);
      };
    };

    return answer;
  };


  return dfs(0);
};


/*

0: [1]
1: [0,  2, 3]
2: [1]
3: [1]


1. Build Graph
2. start 0 DFS until reach restricted node 
  if reach the restricted node update an answer end current search
3. 

*/
