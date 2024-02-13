// 515

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
 // BFS
// Time Complexity: O(n)
// Space Complexity: O(n)
var largestValuesII = function(root) {
  if(!root) {
    return [];
  };

  const helper = (node, answer, level) => {
    if(!node) {
      return;
    };

    const curr = answer[level] === undefined ? -Infinity : answer[level];

    answer[level] = Math.max(node.val, curr);

    helper(node.left, answer, level + 1);
    helper(node.right, answer, level + 1);
  };

  const answer = [];

  helper(root, answer, 0);
    
  return answer;
};

// BFS
// Time Complexity: O(n)
// Space Complexity: O(n)
const largestValues = (root) => {
  if(!root) {
    return [];
  };

  const queue = [];
  const answer = [];
  queue.push(root);

  while(queue.length) {
    const size = queue.length;
    let max = -Infinity;

    for(let i = 0; i < size; i++) {
      const currNode = queue.shift();

      if(currNode.left) {
        queue.push(currNode.left);
      };

      if(currNode.right) {
        queue.push(currNode.right);
      };

      max = Math.max(max, currNode.val);
    };

    answer.push(max);
  };

  return answer;
};

/*

DFS

find max value on each level then add max value to the answer array

*/



