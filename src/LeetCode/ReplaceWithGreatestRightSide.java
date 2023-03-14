package LeetCode;

public class ReplaceWithGreatestRightSide {
    final int[] arr;

    public ReplaceWithGreatestRightSide(int[] arr) {
        this.arr = arr;
    }

    // Time complexity:
    // Space complexity:
    public int[] naive() {
        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {
            int max = Integer.MIN_VALUE;

            for (int j = i + 1; j < n; j++) {
                if (arr[j] > max) {
                    max = arr[j];
                }
            }

            arr[i] = max;
        }

        arr[n - 1] = -1;

        return arr;
    }

    public int[] solution() {
        int max = -1;
        int n = arr.length;
        int tmp;

        for (int i = n - 1; i >= 0; i--) {
            // get current value
            tmp = arr[i];

            // change current value with last max value
            arr[i] = max;

            // get max using current value and last max value
            max = Math.max(tmp, max);
        }

        return arr;
    }
}
