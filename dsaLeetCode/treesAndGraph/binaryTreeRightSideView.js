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


// Time Complexity: O(n)
// Space Complexity: O(n)
const BFS = (root) => {
  if(!root) {
    return [];
  };

  const queue = [root];
  const answer = [];
  
  while(queue.length) {
    const size = queue.length;
  
    answer.push(queue[size - 1].val);
  
    for(let i = 0; i < size; i++) {
      const curr = queue.shift();
  
      if(curr.left) {
        queue.push(curr.left);
      };
  
      if(curr.right) {
        queue.push(curr.right);
      };
    };
  
  };
  
  return answer;
  
};

// Time Complexity: O(n)
// Space Complexity: O(n)
const BFSII = (root) => {
  const rightView = (node, result, depth) => {
    if(!node) {
      return;
    };

    if(result.length === depth) {
      result.push(node.val);
    };

    rightView(node.right, result, depth + 1);
    rightView(node.left, result, depth + 1);
  };

  const result = [];

  rightView(root, result, 0);

  return result;
};

// Time Complexity: O(n)
// Space Complexity: O(n)
const BFSIII = (root) => {
  const rightView = (node, result, depth) => {
    if(!node) {
      return;
    };

    result[depth] = node.val;

    rightView(node.left, result, depth + 1);
    rightView(node.right, result, depth + 1);
  };

  const result = [];

  rightView(root, result, 0);

  return result;
};


console.log(BFSIII(root));

