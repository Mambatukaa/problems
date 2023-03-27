package LeetCode;

public class MaxConesecutiveOnesII {
    private int[] nums;

    public MaxConesecutiveOnesII(int[] nums) {
        this.nums = nums;
    }

//
//    public int naive() {
//        int longestSequence = 0;
//        int n = nums.length;
//
//        for (int i = 0; i < n; i++) {
//            int numZeroes = 0;
//
//            // check every consecutive sequence
//            for (int j = i; j < n; j++) {
//                // count how many 0's
//                if (nums[j] == 0) {
//                    numZeroes += 1;
//                }
//
//
//                // # update answer if it's valid
//                if (numZeroes <= 1) {
//                    longestSequence = Math.max(longestSequence, i - j + 1);
//                }
//            }
//        }
//
//        return longestSequence;
//    }

    public int naive() {
        int max = 0;
        int lastZeroIndex = 0;
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            boolean zeroFound = false;
            int counter = 0;

            for (int j = lastZeroIndex; j < nums.length; j++) {
                if (nums[j] == 0) {
                    if (zeroFound) {
                        continue;
                    }

                    zeroFound = true;
                    lastZeroIndex = j;
                }

                counter++;
            }

            max = Math.max(counter, max);

        }

        return max;
    }

}
