// Recursion
// Space Complexity: O(n)
// Time Complexity: O(n)
const hasPathSum = (root, targetSum) => {
  const pathSum = (root, curr = 0) => {
    if(!root) {
      return false;
    }

    curr += root.value;

    if(!root.left && !root.right) {
      return curr == targetSum;
    }

    const left = pathSum(root.left, curr);
    const right = pathSum(root.right, curr);

    return left || right;
  }

  return pathSum(root, 0)
}

// Iterative
// Space Complexity: O(1)
// Time Complexity: O(n)
const hasPathSumII = (root, targetSum) => {
  if(!root) {
    return false;
  }

  const stack = [[root, 0]];

  while(stack.length) {
    let [currNode, sum] = stack.pop();

     // if both children are null, then the node is a leaf
    if(!currNode.left && !currNode.right) {
      if(sum + currNode.value === targetSum) {
        return true;
      } 

      continue;
    }

    sum += currNode.value;

    if(currNode.right) {
      stack.push([currNode.right, sum]);
    };

    if(currNode.left) {
      stack.push([currNode.left, sum]);
    };
  }

  return false;
}

class BT {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}


const root = new BT(1);

const node1 = new BT(2);
const node2 = new BT(3);

root.left = node1;
root.right = node2;

console.log(hasPathSumII(root, 4), 'answer');
