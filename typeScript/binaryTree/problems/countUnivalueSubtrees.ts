import { TreeNode } from '../lib/TreeNode';

const isUnival = (root: TreeNode | null): boolean => {
  if(!root) {
    return true;
  }

  if(root.left && root.left.val != root.val) {
    return false;
  }

  if(root.right && root.right.val != root.val) {
    return false;
  }

  if(isUnival(root.left) && isUnival(root.right)) {
    return true;
  }

  return false;
}

// Solution from youtube that is google interview 
// Time Complexity: O(n^2)
// Space Complexity: O(n)
const countUnivals = (root: TreeNode | null): number => {
  if(!root) {
    return 0;
  }

  let totalCount: number = countUnivals(root.left) + countUnivals(root.right);

  if(isUnival(root)) {
    totalCount++;
  }

  return totalCount;
}

// Time Complexity: O(n)
// Space Complexity: O(n)
const solution = (root: TreeNode | null): number  => {
  let count: number = 0;


  const dfs = (root: TreeNode | null) => {
    if(!root) {
      return true;
    }

    const left = dfs(root.left);
    const right = dfs(root.right);

    if(left && right) {
      if(root.left && root.left.val !== root.val) {
        return false;
      };

      if(root.right && root.right.val !== root.val) {
        return false;
      }

      count++;
    }

    return true;
  }
  
  dfs(root);

  return count;
}


const node1 = new TreeNode(1);
const node2 = new TreeNode(1);
const node3 = new TreeNode(1);
const node4 = new TreeNode(1);
const node5 = new TreeNode(1);
const node6 = new TreeNode(1);

node1.left = node2;
node1.right = node3;

node2.left = node4;
node2.right = node5;

node3.right = node6;

console.log(solution(node1));
