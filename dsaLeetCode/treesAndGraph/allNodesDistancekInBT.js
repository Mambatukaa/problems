/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} target
 * @param {number} k
 * @return {number[]}
 */
var distanceK = function(root, target, k) {

  // add parent to the nodes
  const dfs = (root, parent) => {
    if(!root) {
      return;
    };

    root.parent = parent;
    dfs(root.left, root);
    dfs(root.right, root);
  };

  dfs(root, null);

  const queue = [target];
  let distance = 0;
  const visited = new Set();

  visited.add(target.val);

  while(queue.length && k > distance) {
    const size = queue.length;

    for(let i = 0; i < size; i++) {
      const node = queue.shift();

      for(const neighbor of [node.left, node.right, node.parent]) {
        if(neighbor && !visited.has(neighbor.val)) {
          queue.push(neighbor);
          visited.add(neighbor.val);
        };
      };
    };

    distance++;
  };

  console.log(queue, 'what what what')

  return queue.map((el) => el.val);
};



/*

  Build graph
  
  Add parent to each nodes.

  Start BFS from target

  Add node.left, node.right, node.parent to the queue with distance 

  if distance === k add nodes to the answer


            0
          /   \
         2     1
              /
            3

      3
      3
        

*/
