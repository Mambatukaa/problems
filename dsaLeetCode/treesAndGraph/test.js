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


const countGoodNodesInBT = (root) => {

  const helper = (root, max) => {
    if(!root) {
      return 0;
    };

    const left = helper(root.left, Math.max(max, root.val)) 
    const right = helper(root.right, Math.max(max, root.val));

    let counter = left + right;

    if(root.val >= max) {
      counter++;
    }

    return counter;
  };

  return helper(root, root.val);
};

const countGoodNodesInBTII = (root) => {
  if(!root) {
    return 0;
  };

  const stack = [];
  stack.push([root, root.val]);

  let answer = 0;

  while(stack.length) {
    const [node, max] = stack.pop();

    if(node.val >= max) {
      answer++;
    };

    if(node.left) {
      stack.push([node.left, Math.max(node.val, max)])
    };

    if(node.right) {
      stack.push([node.right, Math.max(node.val, max)])
    };
  };


  return answer;
};


const root = new TreeNode(3)
const node2 = new TreeNode(1)
const node3 = new TreeNode(4)

const node4 = new TreeNode(3)
const node5 = new TreeNode(1)
const node6 = new TreeNode(5)

root.left = node2;
root.right = node3;

node2.left = node4;
node3.left = node5;
node3.right = node6;

console.log(countGoodNodesInBT(root));

// pass max to the children
// compare current value with max and update
// if currentValue < max update answer
