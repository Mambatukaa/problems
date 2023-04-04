package LeetCode;

public class PlusOne {
    private int[] digits;

    public PlusOne(int[] digits) {
        this.digits = digits;
    }

    // Time complexity: O(n)
    // Space complexity: O(n)
    public int[] naive() {
        int n = digits.length;

        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] != 9) {
                digits[i]++;

                return digits;
            }

            digits[i] = 0;
        }

        // all digits are 9's
        digits = new int[n + 1];
        digits[0] = 1;

        return digits;
    }
}
