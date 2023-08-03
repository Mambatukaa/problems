// Time complexity: O(n)
// Space complexity: O(n)
function preOrderTraversal(root: any) {
  const answer: number[] = [];

  preOrder(root);

  function preOrder(root: any) {
    if(root === null) {
      return [];
    }

    answer.push(root.val);
    preOrder(root.left);
    preOrder(root.right);
  }


  return answer;
}
 // [3,1,2];


// Definition for a binary tree node.
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}


const node1 = new TreeNode(1);


console.log(preOrderTraversal(node1));
