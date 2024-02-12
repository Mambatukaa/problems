class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  };
};


class BinaryTree {
  constructor() {
    this.root = null;
  };


  insert(val) {
    const newNode = new TreeNode(val);

    if(!this.root) {
      this.root = newNode;
    } else {
      const queue = [this.root];

      while(queue.length) {
        const curr = queue.shift();

        if(!curr.left) {
          curr.left = newNode;
          return;
        };

        if(!curr.right) {
          curr.right = newNode;
          return;
        };

        queue.push(curr.left);
        queue.push(curr.right);

      };

    };
  }
};

const root = new TreeNode(8);

const node2 = new TreeNode(3);
const node3 = new TreeNode(10);
const node4 = new TreeNode(1);
const node5 = new TreeNode(6);

const node6 = new TreeNode(14);
const node7 = new TreeNode(4);
const node8 = new TreeNode(7);
const node9 = new TreeNode(13);

root.left = node2;
root.right = node3;

node2.left = node4;
node2.right = node5;

node3.right = node6;

node5.left = node7;
node5.right = node8;

node6.left = node9;


// Time Complexity: O(n)
// Space Complexity: O(n)
const maxAncestorDiff = (root) => {
  if(!root) {
    return null;
  };

  const helper = (node, curMax, curMin) => {
    if(!node) {
      // find diff
      console.log(curMax, '========', curMin)
      return curMax - curMin;
    };

    curMax = Math.max(curMax, node.val);
    curMin = Math.min(curMin, node.val);

    const left = helper(node.left, curMax, curMin);
    const right = helper(node.right, curMax, curMin);

    return Math.max(left, right);
  };


  return helper(root, root.val, root.val);
};

console.log(maxAncestorDiff(root));
/*
 
                   8
                 /   \
                3     10
               / \      \
              1   6      14
                 / \     /
                4   7   13

 */
