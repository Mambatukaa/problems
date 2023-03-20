import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {0, 1, 2, 2, 3, 0, 4, 2};
        int val = 2;

        RemoveElementInOrder removeElementInOrder = new RemoveElementInOrder(nums, val);

        System.out.println(removeElementInOrder.naive());
    }

}
