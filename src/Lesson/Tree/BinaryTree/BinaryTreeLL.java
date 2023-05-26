package Lesson.Tree.BinaryTree;

import java.util.LinkedList;
import java.util.Queue;

public class BinaryTreeLL {
    public BinaryNode root;

    public BinaryTreeLL() {
        this.root = null;
    }

    public void preOrder(BinaryNode node) {
        // Root Node ==> Left Subtree ==> Right Subtree
        if (node == null) {
            return;
        }

        System.out.print(node.value + " ");

        preOrder(node.left);
        preOrder(node.right);
    }

    public void inOrder(BinaryNode node) {
        // Left SubTree ==> Root Node ==> Right Subtree
        if (node == null) {
            return;
        }

        inOrder(node.left);
        System.out.print(node.value + " ");
        inOrder(node.right);

    }

    public void postOrder(BinaryNode node) {
        // Left SubTree ==> Right Subtree ==> Root Node
        if (node == null) {
            return;
        }

        postOrder(node.left);
        postOrder(node.right);
        System.out.print(node.value + " ");

    }

    public void levelOrder() {
        Queue<BinaryNode> queue = new LinkedList<BinaryNode>();

        queue.add(root);

        while (!queue.isEmpty()) {
            BinaryNode presentNode = queue.remove();
            System.out.print(presentNode.value + " ");

            if (presentNode.left != null) {
                queue.add(presentNode.left);
            }

            if (presentNode.right != null) {
                queue.add(presentNode.right);
            }

        }
    }

    // Time complexity: O(n)
    // Space complexity: O(n)
    public Boolean search(String value) {
        Queue<BinaryNode> queue = new LinkedList<BinaryNode>();

        queue.add(root);

        while (!queue.isEmpty()) {
            BinaryNode presentNode = queue.remove();
            if (presentNode.value.equals(value)) {
                System.out.println("Found " + value);

                return true;

            }

            if (presentNode.left != null) {
                queue.add(presentNode.left);
            }

            if (presentNode.right != null) {
                queue.add(presentNode.right);
            }
        }

        System.out.println("Not found");
        return false;
    }

    // Time complexity: O(n)
    // Space complexity: O(n)
    public void insert(String value) {
        // find first vacant place using level order traversal
        // check left or right if each of them doesn't exist insert it this place

        BinaryNode node = new BinaryNode();
        node.value = value;

        if (root == null) {
            root = node;
            return;
        }

        Queue<BinaryNode> queue = new LinkedList<>();

        queue.add(this.root);

        while (!queue.isEmpty()) {
            BinaryNode presentNode = queue.remove();

            if (presentNode.left == null) {
                presentNode.left = node;
                System.out.println("Successfully");
                break;
            } else if (presentNode.right == null) {
                presentNode.right = node;
                break;
            } else {
                queue.add(presentNode.left);
                queue.add(presentNode.right);

            }
        }

    }

    // Space complexity: O(n)
    // Time complexity: O(n)
    public void delete(String value) {
        // set deepest node's value to current node
        Queue<BinaryNode> queue = new LinkedList<BinaryNode>();
        queue.add(root);

        while (!queue.isEmpty()) {
            BinaryNode present = queue.remove();

            if (present.value.equals(value)) {
                // find deepest node
                present.value = getDeepestNode().value;
                // delete deepest node
                deleteDeepestNode();

                System.out.println("The node " + present.value + " is deleted!");

                return;
            }

            if (present.left != null) {
                queue.add(present.left);
            }

            if (present.right != null) {
                queue.add(present.right);
            }

        }
        System.out.println("The node doesn't exist in binary tree.");

    }


    // Time complexity: O(n)
    // Space complexity: O(n)
    public BinaryNode getDeepestNode() {
        Queue<BinaryNode> queue = new LinkedList<BinaryNode>();
        queue.add(root);
        BinaryNode presentNode = null;

        while (!queue.isEmpty()) {
            presentNode = queue.remove();

            if (presentNode.left != null) {
                queue.add(presentNode.left);
            }

            if (presentNode.right != null) {
                queue.add(presentNode.right);
            }
        }

        return presentNode;
    }

    public void deleteDeepestNode() {
        // find the deepest node's parent
        // if present.left doesn't exist remove previous right
        // if present.right doesn't exist remove previous left

        Queue<BinaryNode> queue = new LinkedList<BinaryNode>();

        queue.add(root);

        BinaryNode previousNode, presentNode = null;

        while (!queue.isEmpty()) {
            previousNode = presentNode;
            presentNode = queue.remove();

            if (presentNode.left == null) {
                previousNode.right = null;
                return;
            } else if (presentNode.right == null) {
                previousNode.left = null;
                return;
            }

            queue.add(presentNode.left);
            queue.add(presentNode.right);

        }

    }


    // Time complexity: O(1)
    // Space complexity: O(1)
    public void deleteBT() {
        root = null;

        System.out.println("Binary tree has been successfully deleted.");
    }
}
