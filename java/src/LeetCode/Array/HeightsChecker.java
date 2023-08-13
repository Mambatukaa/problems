package LeetCode.Array;

import java.util.Arrays;

public class HeightsChecker {
    private final int[] heights;

    public HeightsChecker(int[] heights) {
        this.heights = heights;
    }

    // Time complexity: O(log * n) + O(n) => remove constants O(n)
    // Space complexity: O(n)
    public int naive() {
        int counter = 0;
        int[] heights1 = heights.clone();

        Arrays.sort(heights1);

        for (int i = 0; i < heights.length; i++) {
            if (heights1[i] != heights[i]) {
                counter++;
            }
        }

        return counter;
    }


    // Space complexity: O(1)
    // Time complexity: O(n)
    public int solution() {
        int[] heightToFreq = new int[101];

        for (int height : heights) {
            heightToFreq[height]++;
        }

        int result = 0;
        int curHeight = 0;

        for (int height : heights) {
            while (heightToFreq[curHeight] == 0) {
                curHeight++;
            }

            if (curHeight != height) {
                result++;
            }

            heightToFreq[curHeight]--;
        }

        return result;
    }


}
