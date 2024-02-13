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

const node3 = new TreeNode(4);
const node4 = new TreeNode(5);

const node5 = new TreeNode(8);
const node6 = new TreeNode(9);

const node7 = new TreeNode(10);
const node8 = new TreeNode(12);


root.left = node2;

node2.left = node3;
node2.right = node4;

node3.left = node5;
node4.right = node6;

node5.left = node7;
node6.right = node8;


const BFS = (root) => {
  const queue = [];
  queue.push(root);
  let level = 0;

  while(queue.length) {
    const size = queue.length;

    level++;

    for(let i = 0; i < size; i++) {
      const node = queue.shift();

      console.log(node.val, level);

      if(node.left) {
        queue.push(node.left);
      };

      if(node.right) {
        queue.push(node.right);
      };

    };

  };

  return level;
};

// Time Complexity: O(n^2)
// Space Complexity: O(1)
const BFSII = (root) => {
  const findHeight = (root) => {
    if(!root) {
      return 0;
    };

    const leftHeight = findHeight(root.left);
    const rightHeight = findHeight(root.right);

    return 1 + Math.max(rightHeight, leftHeight);
  };

  const processCurrentLevel = (root, level) => {
    if(!root) {
      return;
    };

    if(level === 1) {
      console.log(root.val);
    };

    if(level > 1) {
      processCurrentLevel(root.left, level - 1);
      processCurrentLevel(root.right, level - 1);
    };
  };

  const height = findHeight(root);

  for(let l = 1; l <= height; l++) {
    processCurrentLevel(root, l);
  };

};


console.log(BFSII(root));

