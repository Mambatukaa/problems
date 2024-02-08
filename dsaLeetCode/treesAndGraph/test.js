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

const root = new TreeNode(1);

const node2 = new TreeNode(2);
const node3 = new TreeNode(1);

const node4 = new TreeNode(6);
const node5 = new TreeNode(2);
const node6 = new TreeNode(0);
const node7 = new TreeNode(8);

const node8 = new TreeNode(7);
const node9 = new TreeNode(4);

root.left = node2;
root.right = node3;

node2.left = node4;
node2.right = node5;

node3.left = node6;
node3.right = node7;

node5.left = node8;
node5.right = node9;

const lowestCommonAncestors = (root, p, q) => {
  if(!root) {
    return null;
  }

  if(root.val === p || root.val === q) {
    return root.val;
  }
  const left = lowestCommonAncestors(root.left, p, q);
  const right = lowestCommonAncestors(root.right, p, q);

  if(left !== null && right !== null) {
    return root.val;
  };

  if(left !== null) {
    return left;
  }

  return right;
};


console.log(lowestCommonAncestors(root, 7, 0));

// pass max to the children
// compare current value with max and update
// if currentValue < max update answer
