const sum = (root) => {

}

class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

const root = new BinaryTree(1);

const node2 = new BinaryTree(2);
const node3 = new BinaryTree(3);

const node4 = new BinaryTree(4);
const node5 = new BinaryTree(5);

const node6 = new BinaryTree(6);
const node7 = new BinaryTree(7);

root.left = node2;
root.right = node3;

node2.left = node4;
node2.right = node5;

node3.left = node6;
node3.right = node7;

sum(root);
