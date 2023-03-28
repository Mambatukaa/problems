package LeetCode;

public class MaxConsecutiveOnesII {
    private int[] nums;

    public MaxConsecutiveOnesII(int[] nums) {
        this.nums = nums;
    }


    // Space complexity: O(1)
    // Time complexity: O(n^2)
    public int naiveLC() {
        int longestSequence = 0;

        for (int left = 0; left < nums.length; left++) {
            int numZeroes = 0;

            // check every consecutive sequence
            for (int right = left; right < nums.length; right++) {

                // count how many 0's
                if (nums[right] == 0) {
                    numZeroes += 1;
                }

                // # update answer if it's valid
                if (numZeroes <= 1) {
                    longestSequence = Math.max(longestSequence, right - left + 1);
                }
            }
        }

        return longestSequence;
    }

    // Space complexity: O(1)
    // Time complexity: O(n^2)
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


    // Time complexity: O(n)
    // Space complexity: O(1)
    public int solution() {
        int max = 0;
        int r = 0;
        int l = 0;
        int numZeroes = 0;
        int n = nums.length;

        while (r < n) {
            if (nums[r] == 0) {
                numZeroes++;
            }

            while (numZeroes == 2) {
                if (nums[l] == 0) {
                    numZeroes--;
                }

                l++;
            }

            max = Math.max(max, r - l + 1);

            r++;
        }

        return max;

    }

}
