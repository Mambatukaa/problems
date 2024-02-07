class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  };
};

const node5 = new TreeNode(5);

const node4 = new TreeNode(4);
const node8 = new TreeNode(8);

const node11 = new TreeNode(11);
const node13 = new TreeNode(13);

const node42 = new TreeNode(4);
const node7 = new TreeNode(7);

const node2 = new TreeNode(2);
const node1 = new TreeNode(1);

node5.left = node4;
node5.right = node8

node4.left = node11;
node11.left = node7;

node11.right = node2;

node8.left = node13;
node8.right = node42;

node42.right = node1;



const pathSum = (root, targetSum, sum = 0) => {
  if(!root) {
    return false;
  };

  if(!root.left && !root.right) {

    if(targetSum === sum + root.val) {
      return true;
    };

    return false;
  };

  const leftSum = pathSum(root.left, targetSum, sum + root.val);
  const rightSum = pathSum(root.right, targetSum, sum + root.val);

  return leftSum || rightSum;
};

const pathSumII =(root, targetSum) {
  if(!root) {
    return false;
  };

  const stack = [];
  stack.push([root, root.val]);

  while(stack.length) {
    const [node, sum] = stack.pop();

    if(!node.left && !node.right) {

      if(sum === targetSum) {
        return true;
      };
    }

    if(node.left) {
      stack.push([node.left, sum + node.left.val]);
    };

    if(node.right) {
      stack.push([node.right, sum + node.right.val]);
    };


  };

  return false;
};


console.log(pathSum(node5, 22));
