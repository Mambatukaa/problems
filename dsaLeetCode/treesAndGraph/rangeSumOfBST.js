// 982

 /* Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} low
 * @param {number} high
 * @return {number}
 */

 // Time Complexity: O(log n) // Worst case = O(n)
 // Space Complexity: O(n) 
var rangeSumBSTII = function(root, low, high) {
  if(!root) {
    return 0;
  };

  let answer = 0;
  // root value in range
  if(low <= root.val && root.val <= high) {
    answer += root.val;
  };

  // go right
  if(root.val <= high) {
    answer += rangeSumBST(root.right, low, high);
  };

  // go left
  if(root.val >= low) {
    answer += rangeSumBST(root.left, low, high);
  };
    
  return answer;
};

 // Time Complexity: O(log n) // Worst case = O(n)
 // Space Complexity: O(n)
var rangeSumBST = function(root, low, high) {
  if(!root) {
    return 0;
  };

  const stack = [root];
  let answer = 0;

  while(stack.length) {
    const node = stack.pop();

    // node in range
    if(low <= node.val && node.val <= high ) {
      answer += node.val;
    };

    if(node.left && node.val >= low) {
      stack.push(node.left);
    };

    if(node.right && node.val <= high) {
      stack.push(node.right);
    };

  };

  return answer;
};


/*
low = 7, high = 10;

                    10
                  /   \
                 5     15
                / \     \
               3   7     18


1. Check is node in range if it's in range update answer
2. If node value is not greater than high go right
3. If node value is not less than low go left
4. return answer;


1. Recursive

*/
