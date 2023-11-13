// Time Complexity: O(n)
// Space Complexity: O(n)
const inOrderTraverse = (tree, array) => {
  if(!tree) {
    return array;
  }

  inOrderTraverse(tree.left, array);
  array.push(tree.value);
  return inOrderTraverse(tree.right, array);
}

// Time Complexity: O(n)
// Space Complexity: O(n)
const preOrderTraverse = (tree, array) => {
  if(!tree) {
    return array;
  }

  array.push(tree.value);
  preOrderTraverse(tree.left, array);
  return preOrderTraverse(tree.right, array);
}

// Time Complexity: O(n)
// Space Complexity: O(n)
const postOrderTraverse = (tree, array) => {
  if(!tree) {
    return array;
  }

  postOrderTraverse(tree.left, array);
  postOrderTraverse(tree.right, array);
  array.push(tree.value);
  return array;
}


class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

}


const node1 = new BST(10);

const node2 = new BST(5);
const node3 = new BST(15);

const node4 = new BST(2);
const node5 = new BST(5);

const node6 = new BST(22);
const node7 = new BST(1);


node1.left = node2;
node1.right = node3;

node2.left = node4;
node2.right = node5;

node3.right = node6;
node4.left = node7;

console.log(postOrderTraverse(node1, []))

