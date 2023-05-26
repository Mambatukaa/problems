package Lesson.Tree.BinaryTree;

public class BinaryTree {
    String[] arr;
    int lastUsedIndex;

    // Time complexity: O(1)
    // Space complexity: O(n)
    public BinaryTree(int size) {
        arr = new String[size + 1];
        lastUsedIndex = 0;

        System.out.println("Blank tree of size " + size + " has been created.");
    }

    /*
      Insertion
     */

    boolean isFull() {
        return arr.length - 1 == lastUsedIndex;
    }

    // Space complexity: O(1)
    // Time complexity: O(1)
    public void insert(String value) {
        if (isFull()) {
            System.out.println("Array is full.");
            return;
        }

        arr[lastUsedIndex + 1] = value;
        lastUsedIndex++;
        System.out.println("Successfully inserted.");
    }

    /* Traversal
     * Pre order
     * In order
     * Post
     * Level
     */

    // Time complexity: O(n)
    // Space complexity: O(n)
    public void preOrder(int index) {
        // root => left subChild => right subChild

        if (index > lastUsedIndex) {
            return;
        }

        System.out.print(arr[index] + " ");

        preOrder(index * 2);
        preOrder(index * 2 + 1);
    }

    // Time complexity: O(n)
    // Space complexity: O(n)
    public void inOrder(int index) {
        // left subChild => root => right subChild

        if (index > lastUsedIndex) {
            return;
        }

        inOrder(index * 2);
        System.out.print(arr[index] + " ");
        inOrder(index * 2 + 1);
    }

    // Time complexity: O(n)
    // Space complexity: O(n)
    public void post(int index) {
        // left sub -> rightSub -> root

        if (index > lastUsedIndex) {
            return;
        }

        post(index * 2);
        post(index * 2 + 1);

        System.out.print(arr[index] + " ");
    }


    // Time complexity: O(n)
    // Space complexity: O(1)
    public void level() {
        for (int i = 1; i <= lastUsedIndex; i++) {
            System.out.print(arr[i]);

            if (i != lastUsedIndex) {
                System.out.print(" -> ");
            }
        }
    }


    // Search
    // Time complexity: O(n)
    // Space complexity: O(1)
    public int search(String value) {
        for (int i = 1; i <= lastUsedIndex; i++) {
            if (arr[i].equals(value)) {
                return i;
            }
        }

        return -1;
    }


    // Delete
    // Space complexity: O(1)
    // Time complexity: O(n)
    public void delete(String value) {
        int location = search(value);

        if (location == -1) {
            return;
        }

        arr[location] = arr[lastUsedIndex];
        lastUsedIndex--;

        System.out.println("The Node has been deleted.");
    }


    // Delete binary tree
    public void deleteBT() {
        arr = null;
        lastUsedIndex = 0;

        System.out.println("Successfully deleted a BT.");
    }

}
