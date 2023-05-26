package LeetCode.LinkedList.Design;

public class SinglyLinkedList {
    public Node head;
    public Node tail;
    public int size;

    // Time complexity: O(1)
    // Space complexity: O(1)
    public Node createSinglyLinkedList(int nodeValue) {
        head = new Node();
        Node node = new Node();

        node.value = nodeValue;
        node.next = null;

        head = node;
        tail = node;
        size++;

        return head;
    }


    // Time complexity: O(n)
    // Space complexity: O(1)
    public void insert(int location, int nodeValue) {
        if (size == 0) {
            createSinglyLinkedList(nodeValue);
            return;
        }

        Node node = new Node();
        node.value = nodeValue;

        // beginning
        if (location == 0) {
            node.next = head;
            head = node;

            // end
        } else if (location >= size) {
            node.next = null;
            tail.next = node;
            tail = node;
            // middle
        } else {
            Node curr = head;

            for (int i = 0; i < location - 1; i++) {
                curr = curr.next;
            }

            Node nextNode = curr.next;
            curr.next = node;
            node.next = nextNode;
        }

        size++;
    }


    // Time complexity: O(n)
    // Space complexity: O(1)
    public void traversal() {
        if (head == null) {
            System.out.println("Please create singly linked list first!");
        } else {
            Node tempNode = head;

            for (int i = 0; i < size; i++) {
                System.out.print(tempNode.value);
                if (i != size - 1) {
                    System.out.print(" -> ");
                }

                tempNode = tempNode.next;

            }
            System.out.println();

        }


    }

    // Time complexity: O(n)
    // Space complexity: O(1)
    public boolean search(int nodeValue) {
        if (head != null) {
            Node tempNode = head;

            for (int i = 0; i < size; i++) {
                if (tempNode.value == nodeValue) {
                    System.out.println("Found at index " + i);
                    return true;
                }

                tempNode = tempNode.next;

            }

        }

        System.out.println("Not found");

        return false;
    }


    // Time complexity: O(n)
    // Space complexity: O(1)
    public void delete(int location) {
        if (head == null) {
            System.out.println("SLL not exist");
            return;
        }

        // deleting first element
        if (location == 0) {
            head = head.next;
            size--;

            if (size == 0) {
                head = null;
                tail = null;
            }


            // deleting last element
        } else if (location >= size) {
            Node temp = head;

            for (int i = 0; i < size - 1; i++) {
                temp = temp.next;
            }

            if (temp == head) {
                head = tail = null;
                size--;
                return;
            }

            temp.next = null;
            tail = temp;

            size--;

            // deleting the mid element
        } else {
            Node temp = head;

            for (int i = 0; i < location - 1; i++) {
                temp = temp.next;
            }

            temp.next = temp.next.next;

            size--;
        }

    }

    // Time complexity: O(1)
    // Space complexity: O(1)
    public void deleteEntireSLL() {
        head = null;
        tail = null;

        System.out.println("The SLL deleted successfully");
    }

}