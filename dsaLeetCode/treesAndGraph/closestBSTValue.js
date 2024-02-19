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
 * @param {number} target
 * @return {number}
 */
// Time Complexity: O(log n) // O(n)
// Space Complexity: O(log n) // O(n)
var closestValue = function(root, target) {
  let answer = null;
  let minDiff = Infinity;

  const helper = (root) => {
    if(!root) return;

    const currDiff = Math.abs(target - root.val);

    if(currDiff < minDiff || currDiff === minDiff && root.val < answer) {
      answer = root.val;
      minDiff = currDiff;
    };

    if(root.val > target) {
      return helper(root.left)
    } else {
      return helper(root.right)
    }
  };

  helper(root);


  return answer;
};





/*

        4
      /   \
    2       5
  /   \
1       3

target = 3.5;

root = 4;

diff = 0.5;
answer = 4;

compare target with every node and update answer using diff;
1. if (node.val > target) {
  //go left
  } else {
    //go right
  };
2. return answer

3. if currDiff === 0 return curr.node;

let minDiff = Infinity;
let answer = null;

helper = (root, target) => {
  if(!root) return;

  const currDiff = Math.abs(target - root.val);

  if(currDiff < minDiff) {
    answer = root;
    minDiff = currDiff;
  };

  if(root.val > target) {
    return helper(root.left, target)
  } else {
    return helper(root.right)
  }


};



*/
