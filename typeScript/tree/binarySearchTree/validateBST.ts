import { TreeNode } from '../lib/TreeNode';
// [4,2,5,1,3,6,7];


const node1 = new TreeNode(4);

const node2 = new TreeNode(2);
const node3 = new TreeNode(6);

const node4 = new TreeNode(1);
const node5 = new TreeNode(3);

const node6 = new TreeNode(5);
const node7 = new TreeNode(0);


node1.left = node2;
node1.right = node3;


node2.left = node4;
node2.right = node5;

node3.left = node6;
node3.right = node7;


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

    console.log(prev?.value, curr.value)

    prev = curr.val;

    curr = curr.right;
  }

  return true;
}


// Time Complexity: O(n)
// Space Complexity: O(n) // stack
const isValidBSTIterativeII = (root: TreeNode | null) => {
  const stack: any[] = [];
  const upper: any[] = [];
  const lower: any[] = [];

  const update = (root: TreeNode | null, low: number | null, high: number | null) => {
    stack.push(root);
    lower.push(low);
    upper.push(high);
  }


  const solution = (root: TreeNode | null) => {
    stack.push(root);
    let low = null;
    let high = null;


    while(stack.length) {
      root = stack.shift();
      low = lower.shift();
      high = upper.shift();


      if(root === null) continue;

      const val = root.val;

      if(low !== null && val <= low) {
        return false;
      }

      if(high !== null && val >= high) {
        return false;
      }

      update(root.right, val, high);
      update(root.left, low, val);
    }

    return true;
  }


  return solution(root);
}

console.log(isValidBSTIterativeII(node1));
