class BinaryNode {
  constructor(val) {
    this.val = val;
    this.height = 1;
    this.left = null;
    this.right = null;
  }
}

class AVL {
  constructor() {
    this.root = null;
  }

  levelOrder() {
    if(!this.root) {
      return null;
    }

    let level = 1;
    const queue = [];
    queue.push(this.root);

    while(queue.length) {

      let size = queue.length;

      while(size > 0) {
        size --;

        const current = queue.shift();

        if(current.left) {
          queue.push(current.left);
        }

        if(current.right) {
          queue.push(current.right);
        }

        console.log('level:', level, '====', current.val);
      }

      level++;



    }

  }

  getHeight(node) {
    if(!node) {
      return 0;
    } else {
      return node.height;
    }
  }

  getBalance(node) {
    if(!node) {
      return 0;
    }

    return this.getHeight(node.left) - this.getHeight(node.right);
  }

  rotateRight(disbalancedNode) {
    const newRoot = disbalancedNode.left;

    disbalancedNode.left = disbalancedNode.left.right;

    newRoot.right = disbalancedNode;

    // update height
    disbalancedNode.height = 1 + Math.max(this.getHeight(disbalancedNode.left), this.getHeight(disbalancedNode.right))
    newRoot.height = 1 + Math.max(this.getHeight(newRoot.left), this.getHeight(newRoot.right));

    return newRoot;
  }

  rotateLeft(disbalancedNode) {
    const newRoot = disbalancedNode.right;

    disbalancedNode.right = disbalancedNode.right.left;
    newRoot.left = disbalancedNode;

    // update height;
    disbalancedNode.height = 1 + Math.max(this.getHeight(disbalancedNode.left), this.getHeight(disbalancedNode.right))
    newRoot.height = 1 + Math.max(this.getHeight(newRoot.left), this.getHeight(newRoot.right));

    return newRoot;
  }

  insertion(node, value){
    if(!node) {
      return new BinaryNode(value);
    } else if(node.val > value) {
      node.left = this.insertion(node.left, value);
    } else {
      node.right = this.insertion(node.right, value);
    }

    node.height = 1 + Math.max(this.getHeight(node.left), this.getHeight(node.right));

    const balance = this.getBalance(node);

    console.log(balance, 'haahaha', value)

    // left ==> left
    if(balance > 1 && value < node.left.val) {
      return this.rotateRight(node);
    }

    // left ==> right
    if(balance > 1 && value > node.left.val) {
      node.left = rotateLeft(node.left);

      return this.rotateRight(node);
    }
    
    // right ==> right
    if(balance < 0 && value > node.right.val) {

      return this.rotateLeft(node);
    }

    // right ==> left
    if(balance < 0 && value < node.right.val) {
      node.right = rotateRight(node.right);

      return this.rotateLeft(node);
    }

    return node;
  };

  insert(value) {
    this.root = this.insertion(this.root, value);
  };

  delete(value) {

  }



}


const avl = new AVL();

avl.insert(1);
avl.insert(2);
avl.insert(3);
avl.insert(4);
avl.insert(5);

avl.insert(6);

avl.levelOrder();

/*
                    1
                   /
                  2 
                /
               3
              / \
             4   5
            / 
           6
 */
