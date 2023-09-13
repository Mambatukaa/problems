import { TreeNode } from '../../lib/TreeNode';


// Time Complexity: O(n)
// Space Complexity: O(n)
function isSymmetric(left: TreeNode | null, right: TreeNode | null): boolean {
  if(!left && !right) {
    return true;
  };

  if(!left || !right) {
    return false;
  };


  return (left.val === right.val) && isSymmetric(left.left, right.right) && isSymmetric(left.right, right.left);
}


// Time Complexity: O(n)
// Space Complexity: O(n)
function isSymmetricIteration(left: TreeNode | null, right: TreeNode | null) {
  const queue: any[] = [];

  queue.unshift(left, right);

  while(queue.length) {
    const t1 = queue.shift();
    const t2 = queue.shift();


    if(t1 === null && t2 === null) continue;
    if(t1 === null || t2 === null) return false;
    if(t1.val !== t2.val) return false;

    queue.unshift(t1.left);
    queue.unshift(t2.right);
    queue.unshift(t1.right);
    queue.unshift(t2.left);
  }

  return true;
}


const node1 = new TreeNode(1);
const node2 = new TreeNode(2);
const node3 = new TreeNode(2);
const node4 = new TreeNode(3);
const node5 = new TreeNode(3);
const node6 = new TreeNode(4);
const node7 = new TreeNode(4);

node1.left = node2;
node1.right = node3;

node2.left = node4;
node2.right = node6;


node3.left = node7;
node3.right = node5;


console.log(isSymmetric(node1.left, node1.right));
console.log(isSymmetricIteration(node1.left, node1.right));
