class TreeNode {
  val;
  left;
  right;

  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

// const root = new TreeNode(2);
// const node2 = new TreeNode(1);
// const node3 = new TreeNode(3);

// root.left = node2;
// root.right = node3;

// let prev;

// const isValidBST = (root) => {
//   if(!root) {
//     return true;
//   }

//   if(!isValidBST(root.left)) {
//     return false;
//   }

//   if(prev && prev.val > root.val) {
//     return false;
//   }

//   prev = root;

//   if(!isValidBST(root.right)) {
//     return false;
//   }

//   return true;
// }

// console.log(isValidBST(root));

// [4,2,5,1,3,6,7];

const node1 = new TreeNode(4);

const node2 = new TreeNode(2);
const node3 = new TreeNode(6);

const node4 = new TreeNode(1);
const node5 = new TreeNode(3);

const node6 = new TreeNode(5);
const node7 = new TreeNode(7);

node1.left = node2;
node1.right = node3;

node2.left = node4;
node2.right = node5;

node3.left = node6;
node3.right = node7;

// Time Complexity: O(n)
// Space Complexity: O(1)
const isValidBSTIterative = root => {
  const stack = [];
  const upper = [];
  const lower = [];

  const update = (root, low, high) => {
    stack.push(root);
    lower.push(low);
    upper.push(high);
  };

  const solution = root => {
    stack.push(root);
    let low = null;
    let high = null;

    while (stack.length) {
      root = stack.shift();
      low = lower.shift();
      high = upper.shift();

      if (root === null) continue;

      const val = root.val;

      if (low !== null && val <= low) {
        return false;
      }

      if (high !== null && val >= high) {
        return false;
      }

      update(root.left, low, val);
      update(root.right, val, high);
    }

    return true;
  };

  return solution(root);
};

console.log(isValidBSTIterative(node1));
