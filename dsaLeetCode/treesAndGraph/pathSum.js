// Space Complexity: O(n)
// Time Complexity: O(n)
//
const hasPathSum = (root, targetSum) => {
  const pathSum = (root, curr = 0) => {
    if(!root) {
      return false;
    }

    curr += root.value;

    if(!root.left && !root.right && curr == targetSum) {
      return true;
    }

    const left = pathSum(root.left, curr);
    const right = pathSum(root.right, curr);

    return left || right;
  }

  return pathSum(root, 0)
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

console.log(hasPathSum(root, 4), 'answer');
