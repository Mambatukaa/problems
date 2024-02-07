class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  };
};

const node1 = new TreeNode(3);

const node1Left = new TreeNode(9);
const node1Right = new TreeNode(20);

const node1RightLeft = new TreeNode(15);
const node1RightRight = new TreeNode(7);

node1.left = node1Left;
node1.right = node1Right;

node1Right.left = node1RightLeft;
node1Right.right = node1RightRight;



const maxDepth = (root) => {
  if(!root) {
    return 0;
  };

  const leftLevel = maxDepth(root.left);
  const rightLevel = maxDepth(root.right);

  return Math.max(leftLevel, rightLevel) + 1;
};

const maxDepthII = (root) => {
  if(!root) {
    return 0;
  }

  const stack = [];
  stack.push([root, 1]);
  let maxLevel = 0;

  while(stack.length) {
    const [curr, level] = stack.pop();

    maxLevel = Math.max(level, maxLevel);

    if(curr.left) {
      stack.push([curr.left, level + 1]);
    };

    if(curr.right) {
      stack.push([curr.right, level + 1]);
    };
  };

  return maxLevel;
};

console.log(maxDepth(node1));

