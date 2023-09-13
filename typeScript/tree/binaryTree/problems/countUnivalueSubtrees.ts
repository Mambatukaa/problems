import { TreeNode } from '../../lib/TreeNode';

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
// Solution with global variable
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

// Time Complexity: O(n)
// Space Complexity: O(n)
// No global variable
const solution1 = (root: TreeNode | null) => {
  const dfs = (node: TreeNode | null) => {
    if(!node) {
      return {
        key: true,
        value: 0
      }
    }

    const left: {key: boolean, value: number} = dfs(node.left);
    const right: {key: boolean, value: number} = dfs(node.right);

    const isLeftUniValue: boolean = left.key;
    const isRightUniValue: boolean = right.key;

    const count: number = left.value + right.value;

    if(isLeftUniValue && isRightUniValue) {
      if(node.left && node.left.val !== node.val) {
        return {
          key: false,
          value: count
        }
      }

      if(node.right && node.right.val !== node.val) {
        return {
          key: false,
          value: count
        }
      }

      return {
        key: true,
        value: count + 1
      }

    }

    return {
      key: false,
      value: count
    }
  }


  return dfs(root).value;
}

// Time Complexity: O(n)
// Space Complexity: O(n)
// No global variable
const solution2 = (root: TreeNode | null): number => {
  const count = [0];

  const dfs = (node: TreeNode | null, count: number[]): boolean => {
    if(!node) {
      return true;
    }

    const left: boolean = dfs(node.left, count);
    const right: boolean = dfs(node.right, count);

    if(left && right && (!node.left || node.left.val === node.val) && (!node.right || node.right.val === node.val) ) {
      count[0]++;

      return true;
    }

    return false;
  }

  dfs(root, count);

  return count[0];
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

console.log(solution2(node1));
