package LeetCode.Array;

public class FindEvenNumbersDigit {
    final private int[] nums;


    public FindEvenNumbersDigit(int[] nums) {
        this.nums = nums;
    }

    // Time complexity: O(n) maybe O(n^2) because of an integer convert
    // Space complexity: O(1)
    public int naive() {
        int counter = 0;

        for (int num : nums) {
            int numLength = Integer.toString(num).length();

            if (numLength % 2 == 0) {
                counter++;
            }

        }

        return counter;
    }

    // Time complexity: O(nxm)
    // Space complexity: O(n)
    public int solution() {
        int counter = 0;

        for (int num : nums) {
            int count = 0;

            while (num > 0) {
                num /= 10;
                count++;
            }

            if (count % 2 == 0) {
                counter++;
            }
        }

        return counter;

    }


}
