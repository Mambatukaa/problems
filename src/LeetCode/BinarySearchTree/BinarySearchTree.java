package LeetCode.BinarySearchTree;

import java.util.LinkedList;
import java.util.Queue;

public class BinarySearchTree {
    public BinaryNode root;

    // creation
    // Time complexity: O(1)
    // Space complexity: O(1)
    public BinarySearchTree() {
        root = null;
    }


    // Insertion
    private BinaryNode insert(BinaryNode currentNode, int value) {
        // find location
        // put value
        if (currentNode == null) {
            currentNode = new BinaryNode();
            currentNode.value = value;

            System.out.println("Successfully inserted.");

            return currentNode;
        } else if (value <= currentNode.value) {
            currentNode.left = insert(currentNode.left, value);

            return currentNode;
        } else {
            currentNode.right = insert(currentNode.right, value);

            return currentNode;
        }
    }

    public void insert(int value) {
        root = insert(root, value);
    }


    // Time complexity: O(n)
    // Space complexity: O(n)
    public void preOrder(BinaryNode node) {
        // root --> leftSubTree --> rightSubTree
        if (node == null) {
            return;
        }

        System.out.print(node.value + " ");
        preOrder(node.left);
        preOrder(node.right);
    }

    // Time complexity: O(n)
    // Space complexity: O(n)
    public void inOrder(BinaryNode node) {
        // leftSubTree ==> root ==> rightSubTree

        if (node == null) {
            return;
        }

        inOrder(node.left);
        System.out.print(node.value + " ");
        inOrder(node.right);
    }

    // Time complexity: O(n)
    // Space complexity: O(n)
    public void post(BinaryNode node) {
        // leftSubTree ==> rightSubTree ==> root

        if (node == null) {
            return;
        }

        post(node.left);
        post(node.right);
        System.out.print(node.value + " ");

    }

    // Space complexity: O(n)
    // Time complexity: O(n)
    public void levelOrder() {
        if (root == null) {
            return;
        }

        Queue<BinaryNode> queue = new LinkedList<BinaryNode>();
        queue.add(root);

        while (!queue.isEmpty()) {
            BinaryNode currentNode = queue.remove();

            System.out.print(currentNode.value + " ");

            if (currentNode.left != null) {
                queue.add(currentNode.left);
            }

            if (currentNode.right != null) {
                queue.add(currentNode.right);
            }
        }
    }


    // while
    // Time complexity: O(n)
    //  Space complexity: O(1)
    public Boolean search(int value) {
        BinaryNode currentNode = root;
        // value < root ==> go left
        // value > root ==> go right

        while (currentNode != null) {
            System.out.println(currentNode.value + " search");
            if (value < currentNode.value) {
                currentNode = currentNode.left;
            } else if (value > currentNode.value) {
                currentNode = currentNode.right;
            } else {
                return true;
            }

        }

        return false;
    }

    // Time complexity: O(n)
    // Space complexity: O(n)
    public Boolean searchRecursive(BinaryNode node, int value) {
        if (node != null) {
            System.out.println(node.value);
        }

        if (node == null) {
            return false;
        } else if (node.value == value) {
            return true;
        } else if (node.value < value) {
            // go right
            return searchRecursive(node.right, value);
        } else {
            // go left
            return searchRecursive(node.left, value);
        }
    }

    ;

    public void delete() {
        // leaf node
        // the node has one child
        //
    }

}
