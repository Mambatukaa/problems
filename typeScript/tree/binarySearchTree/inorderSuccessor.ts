import { TreeNode } from '../lib/TreeNode';


const node1 = new TreeNode(5);
const node2 = new TreeNode(3);
const node3 = new TreeNode(6);


const node4 = new TreeNode(2);
const node5 = new TreeNode(4);
const node6 = new TreeNode(1);



node1.left = node2;
node1.right = node3;

node2.left = node4;
node2.right = node5;

node4.left = node6;


// Time complexity: O(n);
// Space complexity: O(n);
const solution = (root: TreeNode | null, p: number) => {
  const answer: number[] = [];

  const inOrder = (root: TreeNode | null) => {
    if(!root) {
      return;
    }

    inOrder(root.left);
    answer.push(root.val);
    inOrder(root.right);
  }


  inOrder(root);


  const idx = answer.indexOf(p);

  if(idx === -1) {
    return null;
  }

  if(answer[idx + 1] !== undefined) {
    return answer[idx+1];
  }

  return null;
};

console.log(solution(node1, 6));
