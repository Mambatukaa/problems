/*

                   1
                 /   \
                2     3
               / \   / \
              4   5 6   7
             /
            8
 
 */


import { TreeNode } from './lib/TreeNode';

const root = new TreeNode(1);
const node2 = new TreeNode(2);
const node3 = new TreeNode(3);
const node4 = new TreeNode(4);
const node5 = new TreeNode(5);
const node6 = new TreeNode(6);
const node7 = new TreeNode(7);
const node8 = new TreeNode(8);


root.left = node2;
root.right = node3;

node2.left = node4;
node2.right = node5;

node3.left = node6;
node3.right = node7

node4.left = node8;

// iteration
// Time Complexity: O(n)
// Space Complexity: O(1)
const BFSI = (root: TreeNode | null) => {
  if(!root) {
    return;
  }

  const answer: any[][] = [];

  const queue: any[] = [];
  queue.push(root);

  while(queue.length) {
    const size = queue.length;
    const subAnswer: any[] = [];

    for(let i = 0; i < size; i++) {
      const curr = queue.shift();
      subAnswer.push(curr.val);

      if(curr.left) {
        queue.push(curr.left);
      }

      if(curr.right) {
        queue.push(curr.right);
      }
    }

    answer.push(subAnswer);

  }

  console.log(answer);


  return answer;
}


// recursion
// Time Complexity: O(n)
// Space Complexity: O(n)
const BFSR = (root: TreeNode | null) => {
  const answer: number[][] = [];
  let level = 0;

  const helper = (root: TreeNode | null, level: number) => {
    if(!root) {
      return;
    }

    if(!answer[level]) {
      answer[level] = [];
    }

    answer[level].push(root.val);


    helper(root.left, level + 1);
    helper(root.right, level + 1);
  }

  helper(root, level);
  console.log(answer);
}


BFSR(root);
