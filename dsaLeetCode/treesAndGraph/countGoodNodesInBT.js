// Recursive
// Time Complexity: O(n)
// Space Complexity: O(n)
const countGoodNodes = (root) => {
  const count = (root, currMax) => {
    // base case
    if(!root) {
      return 0;
    }

    const left = count(root.left, Math.max(root.val, currMax));
    const right = count(root.right, Math.max(root.val, currMax));

    let answer = left + right;

    if(root.val >= currMax) {
      answer++;
    }

    return answer;
  }

  count(root, -Infinity);
}


class BT {
  constructor(val) {
    this.val = val;

    this.left = null;
    this.right = null;
  }
}

const root = new BT(3);

const node1 = new BT(1);
const node2 = new BT(4);

const node3 = new BT(4);
const node4 = new BT(5);

root.left = node1;
root.right = node2;

node1.left = node3;
node2.right = node4;

console.log('answer:', countGoodNodes(root));
