import { TreeNode } from '../binaryTree/lib/TreeNode';
// [4,2,5,1,3,6,7];


const node1 = new TreeNode(0);

const node2 = new TreeNode(2);
const node3 = new TreeNode(6);

const node4 = new TreeNode(1);
const node5 = new TreeNode(3);

const node6 = new TreeNode(5);
const node7 = new TreeNode(0);


// in order traversal
// Time Complexity: O(n)
// Space Complexity: O(n)
const isValidBST = (root: TreeNode | null) => {
  let prev: TreeNode;

  const isValid = (root: TreeNode | null) => {
    if(!root) {
      return true;
    }

    if(!isValid(root.left)) {
      return false;
    }

    console.log(root.val);

    if(prev && prev.val > root.val) {
      return false;
    }

    prev = root;


    if(!isValid(root.right)) {
      return false;
    }

    return true;
  }

  return isValid(root);
}

// Time Complexity: O(n)
// Space Complexity: O(n)
const isValidBSTII = (root: TreeNode | null) => {
  const isValid = (root: TreeNode | null, low: number | null, high: number | null): boolean => {
    if(!root) {
      return true;
    }

    console.log(root.val, low, high);

    if(low !== null && low >= root.val || high !== null && high <= root.val) {
      return false;
    }


    return isValid(root.left, low, root.val) && isValid(root.right, root.val, high);
  }

  return isValid(root, null, null);
}


// Time Complexity: O(n)
// Space Complexity: O(n) // stack
const isValidBSTIterative = (root: TreeNode | null): boolean => {
  const stack: Array<TreeNode> = [];
  let curr: any = root;
  let prev: any = null;

  while(curr || stack.length) {
    while(curr) {
      stack.push(curr);

      curr = curr.left;
    }

    curr = stack.pop();

    if(prev !== null && prev >= curr.val) {
      return false;
    }

    prev = curr.val;

    curr = curr.right;
  }

  return true;
}

console.log(isValidBSTIterative(node1));
