/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
// Time Complexity: O(n + e)
// Space Complexity: O(n)
var canVisitAllRooms = function(rooms) {
  const n = rooms.length;
  const graph = new Map();

  // build graph
  for(let i = 0; i < n; i++) {
    graph.set(i, rooms[i]);
  };

  const stack = [0];
  const visited = new Array(rooms.length).fill(0);

  // dfs
  while(stack.length) {
    const currNode = stack.pop();
    visited[currNode] = 1; 
    const neighbors = graph.get(currNode);

    for(const neighbor of neighbors) {
      if(visited[neighbor] !== 1) {
        stack.push(neighbor);
      };
    };

  };

  return !visited.includes(0);
};

// Time Complexity: O(n + e)
// Space Complexity: O(n)
var canVisitAllRoomsIterative = function(rooms) {
  const stack = [0];
  const visited = new Set();
  visited.add(0);

  while(stack.length) {
    console.log(stack)
    const node = stack.pop();
    const neighbors = rooms[node];

    for(const neighbor of neighbors) {
      if(!visited.has(neighbor)) {
        visited.add(neighbor);
        stack.push(neighbor);
      };

    };
  };

  return visited.size === rooms.length;
};

// Time Complexity: O(n)
// Space Complexity: O(n)
var canVisitAllRooms = function(rooms) {
  const visited = new Set();
  visited.add(0);

  const dfs = (node) => {
    const neighbors = rooms[node];

    for(const neighbor of neighbors) {
      if(!visited.has(neighbor)) {
        visited.add(neighbor);
        dfs(neighbor);
      };
    };
  };

  dfs(0);

  return visited.size === rooms.length;
};


/*

rooms = [[1], [2], [3], []];

The room 0 is only unlocked.

For this example get 1 key from room 0. Then go to the room 1 and get room 2's key... Successfully visited all rooms



Build graph

0: 1
1: 2
2: 3
3: 

Do DFS or BFS and mark all visited rooms. After dfs check all rooms visited or not.

visited = set();
visitedRoomsCount = 0;

*/
