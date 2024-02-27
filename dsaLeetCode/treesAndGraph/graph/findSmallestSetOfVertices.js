/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
 // Time Complexity: O(n)
 // Space Complexity: O(n)
var findSmallestSetOfVertices = function(n, edges) {

  const seen = new Set();

  for(const edge of edges) {
    seen.add(edge[1]);
  };

  const answer = [];

  for(let i = 0; i < n; i++) {
    if(!seen.has(i)) {
      answer.push(i);
    }
  }

  return answer;
};

 // Time Complexity: O(n)
 // Space Complexity: O(n)
 //  
var findSmallestSetOfVerticesII = function(n, edges) {

  const graph = new Map();
  // build graph
  for(let i = 0; i < n; i++) {
    graph.set(i, []);
  };


  for(const [from, to] of edges) {
    graph.get(to).push(from);
  };

  const answer = [];

  for(const [key, value] of graph) {
    if(!value.length) {
      answer.push(key);
    }
  }

  return answer;
};




/*


Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]


// From to

Find all starting nodes.

1. Build graph
2. Return nodes that has no connection from other nodes


*/
