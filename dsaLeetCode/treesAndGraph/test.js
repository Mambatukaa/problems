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


// BFS
// Time Complexity: O(n)
// Space Complexity: O(n)
const zigZag = (root) => {
  if(!root) {
    return [];
  };

  const queue = [];
  const answer = [];
  let leftToRight = true;
  
  queue.push(root);

  while(queue.length) {
    const size = queue.length;
    const arr = [];

    for(let i = 0; i < size; i++) {
      const curr = queue.shift();

      if(leftToRight) {
        arr.push(curr.val);
      } else {
        arr.unshift(curr.val);
      }

      if(curr.left) {
        queue.push(curr.left);
      };

      if(curr.right) {
        queue.push(curr.right);
      };
    };

    leftToRight = !leftToRight;

    answer.push(arr);
  };

  return answer;
};

// DFS
// Time Complexity: O(n)
// Space Complexity: O(n)
const zigZagRecursive = (root, answer, depth = 0) => {
  if(!root) {
    return;
  };

  if(answer[depth] === undefined) answer[depth] = [];

  if(depth % 2 === 0) {
    answer[depth].push(root.val);
  } else {
    answer[depth].unshift(root.val);
  };

  zigZagRecursive(root.left, answer, depth + 1);
  zigZagRecursive(root.right, answer, depth + 1);
};

const answer = [];

zigZagRecursive(root, answer, 0)

console.log(answer);
