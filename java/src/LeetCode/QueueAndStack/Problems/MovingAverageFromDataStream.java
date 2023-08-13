package LeetCode.QueueAndStack.Problems;

import java.util.ArrayDeque;
import java.util.Deque;

public class MovingAverageFromDataStream {
    public int size;
    Deque window = new ArrayDeque<Integer>();
    public int sum = 0;

    public MovingAverageFromDataStream(int size) {
        this.size = size;
    }

    // Space complexity: O(k) k = length of window
    // Time complexity: O(1)
    public double next(int val) {
        window.add(val);

        int first = window.size() > size ? (int) window.poll() : 0;
        sum += val - first;


        return 1.0 * sum / window.size();
    }

}
