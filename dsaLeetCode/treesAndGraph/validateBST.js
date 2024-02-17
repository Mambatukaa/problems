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
 * @return {boolean}
 */
 // Time Complexity: O(n)
 // Space Complexity: O(n)
var isValidBSTII = function(root, min = -Infinity, max = Infinity) {
  if(!root) {
    return true;
  };

  if(min >= root.val || root.val >= max) {
    return false;
  };

  return isValidBST (root.left, min, root.val) && isValidBST(root.right, root.val, max);
};


 // Time Complexity: O(n)
 // Space Complexity: O(n)
const isValidBSTI = (root) => {
  if(!root) {
    return true;
  };

  const stack = [[root, -Infinity, Infinity]];

  while(stack.length) {
    const [curr, min, max] = stack.pop();

    if(curr.val <= min || curr.val >= max) {
      return false;
    };

    if(curr.left) {
      stack.push([curr.left, min, curr.val]);
    };

    if(curr.right) {
      stack.push([curr.right, curr.val, max]);
    };
  };


  return true;
};

 // Time Complexity: O(n)
 // Space Complexity: O(n)
const isValidBST = (root) => {
  let prev = -Infinity;

  const inorder = (root) => {
    if(!root) return true;

    if(!inorder(root.left) || prev >= root.val) {
      return false;
    };

    prev = root.val;

    return inorder(root.right);
  };


  return inorder(root);
};

/*

in order validate check



*/
