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
 * @return {number}
 */
 // Time Complexity: O(n)
 // Space Complexity: O(n)
 // In order traversal
var getMinimumDifference = function(root) {

  let minDifference = Infinity;
  let prev = null;;

  const helper = (root) => {
    if(!root) {
      return;
    };

    helper(root.left);

    if(prev && root.val - prev.val < minDifference) {
      minDifference = root.val - prev.val;
    };

    prev = root;

    helper(root.right);
  };

  helper(root);

  return minDifference;
};

// Time Complexity: O(n)
// Space Complexity: O(n)
const getMinimumDifferenceII = (root) => {
  const stack = [];
  let curr = root;
  let prev = null;
  let min = Infinity;

  while(curr || stack.length) {

    while(curr) {
      stack.push(curr);
      
      curr = curr.left;
    };

    const node = stack.pop();

    console.log(node.val)

    if(prev !== null && node.val - prev < min) {
      min = node.val - prev;
    };

    prev = node.val;

    curr = node.right;
  };


  return min
};

class BinaryNode {
  constructor(val) {
    this.val = val;
    this.right = null;
    this.left = null;
  };
};

const root = new BinaryNode(0);

const node2 = new BinaryNode(2236);
const node3 = new BinaryNode(1277);

const node4 = new BinaryNode(2776);
const node5 = new BinaryNode(519);

root.right = node2;
node2.left = node3;
node2.right = node4;
node3.left = node5;

console.log(getMinimumDifferenceII(root), 'hahahhn');


/*

Binary search tree


             8
          /     \
        5         11 
      /   \       
    1       7

----------------------------------------------------------------------------

             5
          /     \
        0         48 
                /    \       
              12      49


(48, 49) ===> 1 min difference....

root 5



any two different nodes

1. Brute force: Time Complexity: O(n^2) 
2. 


in order traversal

compare prev value with currentValue

and update the answer

*/
