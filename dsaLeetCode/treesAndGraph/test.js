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

const sameTree = (p, q) => {
  if(!p && !q) {
    return true;
  };

  if(!p || !q) {
    return false;
  }

  if(p.val !== q.val) {
    return false;
  };

  return sameTree(p.left, q.left) && sameTree(p.right, q.right); 
};


const isSameTree = (p, q) => {
  if(!p && !q) {
    return false;
  };

  const stack = [];

  stack.push([p, q]);

  while(stack.length) {
    const [pNode, qNode] = stack.pop();

    if(!pNode && !qNode) {
      continue;
    };

    if(!pNode || !qNode) {
      return false;
    }

    if(pNode.val !== qNode.val) {
      return false;
    };

    stack.push([pNode.left, qNode.left]);
    stack.push([pNode.right, qNode.right]);
  };


  return true

};

const pRoot = new TreeNode(1)
const pNode2 = new TreeNode(2)
const pNode3 = new TreeNode(3)

pRoot.left = pNode2;
pRoot.right = pNode3;

const qRoot = new TreeNode(1)
const qNode2 = new TreeNode(2)
const qNode3 = new TreeNode(3)

qRoot.left = qNode2;
qRoot.right = qNode3;

console.log(isSameTree(pRoot, qRoot));

// pass max to the children
// compare current value with max and update
// if currentValue < max update answer
