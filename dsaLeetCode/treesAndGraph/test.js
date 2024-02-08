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
const node3 = new TreeNode(3);
const node4 = new TreeNode(4);
const node5 = new TreeNode(5);


root.right = node2;
node2.right = node3;
node3.right = node4;
node4.right = node5;


const minDepth = (root) => {
  if(!root) {
    return 0;
  };

  if(!root.left) {
    return 1 + minDepth(root.right);
  } else if(!root.right) {
    return 1 + minDepth(root.left);
  };

  const left = 1 + minDepth(root.left);
  const right = 1 + minDepth(root.right);

  return Math.min(left, right);
}

const minDepthII = (root) => {
  if(!root) {
    return 0;
  };


  const stack = [[root, 1]];
  let min = Infinity;

  while(stack.length) {
    const [node, depth] = stack.pop();

    if(!node.left && !node.right) {
      min = Math.min(depth, min);
    }

    if(node.left) {
      stack.push([node.left, depth + 1]);
    };

    if(node.right) {
      stack.push([node.right, depth + 1]);
    };

  };

  return min;

};

console.log(minDepthII(root));

// pass max to the children
// compare current value with max and update
// if currentValue < max update answer
