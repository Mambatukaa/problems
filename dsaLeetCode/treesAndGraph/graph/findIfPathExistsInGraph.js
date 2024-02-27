/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
 // Time Complexity: O(n + m) // n - nodes, m-edges
 // Space Complexity: O(n + m)
var validPathII = function(n, edges, source, destination) {
  if(source === destination) {
    return true;
  }

  // undirected graph
  const graph = new Map();

  for(let i = 0; i < n; i++) {
    graph.set(i, []);
  };

  for(const [from, to] of edges) {
    graph.get(from).push(to);
    graph.get(to).push(from);
  };

  const stack = [source];
  const visited = new Set();
  visited.add(source);

  while(stack.length) {
    const node = stack.pop();
    const neighbors = graph.get(node);

    for(const neighbor of neighbors) {
      if(neighbor === destination) {
        return true;
      };

      if(!visited.has(neighbor)) {
        visited.add(neighbor);
        stack.push(neighbor);
      };
    };

  };

  
  return false;
};

/*

1. Build graph using edges
2. Do the dfs from source
3. If visit destination return true
4. return false after dfs


*/
