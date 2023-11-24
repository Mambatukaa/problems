class BinaryNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Space Complexity: O(n)
// Time Complexity: O(n)
const isValidBst = (root, min, max) => {
  if(root === null) {
    return true;
  }

  console.log(root.value, min, max)

  if(root.value < min || root.value >= max) return false;

  const isLeftValid = isValidBst(root.left, min, root.value);
  const isRightValid = isValidBst(root.right, root.value, max);

  return isLeftValid && isRightValid;
}

const node1 = new BinaryNode(10);
const node2 = new BinaryNode(5);
const node3 = new BinaryNode(1);

node1.left = node2;
node1.right = node3;

console.log(isValidBst(node1, -Infinity, Infinity));
