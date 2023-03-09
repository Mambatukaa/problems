import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] nums = {0, 1, 2, 2, 3, 0, 4, 2};
        int value = 2;

        RemoveElement removeElement = new RemoveElement(nums, value);

        System.out.println(removeElement.naive());


    }

}
