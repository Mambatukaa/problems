import LeetCode.*;

import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] heights = {5, 1, 2, 3, 4};

        HeightsChecker heightsChecker = new HeightsChecker(heights);

        System.out.println(heightsChecker.solution());
    }

}
