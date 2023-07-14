package LeetCode.QueueAndStack;

public class MyCircularQueue {
    public int[] data;
    public int headIndex;
    public int tailIndex;
    public int size;

    public MyCircularQueue(int k) {
        this.data = new int[k];

        this.headIndex = -1;
        this.tailIndex = -1;

        this.size = k;
    }

    public boolean enQueue(int value) {
        if (isFull()) {
            System.out.println("Queue is full");

            return false;
        }

        if (isEmpty()) {
            headIndex = 0;
        }

        tailIndex = (tailIndex + 1) % size;

        data[tailIndex] = value;

        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) {
            System.out.println("Queue is empty");
            return false;
        }

        if (headIndex == tailIndex) {
            headIndex = -1;
            tailIndex = -1;

            return true;
        }

        headIndex = (headIndex + 1) % size;

        return true;
    }

    public int Front() {
        if (!isEmpty()) {
            return -1;
        }

        return data[headIndex];
    }

    public int Rear() {
        if (isEmpty()) {
            return -1;
        }

        return data[tailIndex];

    }

    public boolean isEmpty() {
        return headIndex == -1;
    }

    public boolean isFull() {
        return ((tailIndex + 1) % size) == headIndex;
    }

    public void traversal() {
        if(isEmpty()) {
            System.out.println("Queue is empty");
            return;
        }

        int i = headIndex;

        while(i != tailIndex) {
            System.out.print(data[i] + " -> ");

            i = (i + 1) % size;
        }

        System.out.print(data[tailIndex]);
        System.out.println();

    }

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
}
