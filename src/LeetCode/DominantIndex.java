package LeetCode;

public class DominantIndex {
    private int[] nums;

    public DominantIndex(int[] nums) {
        this.nums = nums;
    }

    // Time complexity: O(n)
    // Space complexity: O(1)
    public int naive() {
        int maxIndex = 0;
        int n = nums.length;

        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[maxIndex]) {
                maxIndex = i;
            }
        }

        for (int i = 0; i < n; i++) {
            if (i == maxIndex) {
                continue;
            }

            if (nums[i] * 2 > nums[maxIndex]) {
                return -1;
            }
        }

        return maxIndex;
    }


    // solution, that earned most vote, from Discussion
    public int solution() {
        // first max
        // second max
        // return secondMax * 2 > max ? -1 : firstMaxIndex
        int max = -1;
        int second = -1;
        int index = -1;
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            if (nums[i] > max) {
                second = max;
                max = nums[i];
                index = i;
            } else if (nums[i] > second) {
                second = nums[i];
            }
        }

        return second * 2 > max ? -1 : index;
    }


}
