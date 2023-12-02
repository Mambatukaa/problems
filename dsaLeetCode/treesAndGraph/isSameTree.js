// Recursive
// Time Complexity: O(n)
// Space Complexity: O(n)
const isSameTree = (p, q) => {
  if(!p && !q) {
    return true;
  }

  if(!p || !q) {
    return false;
  }

  if(p.val !== q.val) {
    return false;
  }

  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}

// Iterative
// Time Complexity: O(n)
// Space Complexity: O(n)
const isSameTreeII = (p, q) => {
  if(!p && !q) {
    return true;
  }

  const stack = [[p, q]];

  while(stack.length) {
    const [p, q] = stack.pop();

    if(!p && !q) {
      continue;
    }

    if(!p || !q) {
      return false;
    }

    if(p.val !== q.val) {
      return false;
    }

    stack.push([p.left, q.left]);
    stack.push([p.right, q.right]);
  }

  return true;
}

class BT {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}


const pRoot = new BT(1);

const pNode1 = new BT(2);
const pNode2 = new BT(3);

const qRoot = new BT(1);

const qNode1 = new BT(2);
const qNode2 = new BT(3);

pRoot.left = pNode1;
pRoot.right = pNode2;

qRoot.left = qNode1;
qRoot.right = qNode2;

console.log('answer:', isSameTreeII(pRoot, qRoot));
