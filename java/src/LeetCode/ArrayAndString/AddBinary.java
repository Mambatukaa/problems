package LeetCode.ArrayAndString;

public class AddBinary {
    final private String a;
    final private String b;

    public AddBinary(String a, String b) {
        this.a = a;
        this.b = b;
    }


    // Time complexity: O(n)
    // Space complexity:  O(n)

    public String naive() {
        int n = a.length();
        int m = b.length();

        StringBuilder res = new StringBuilder();
        int j = m - 1;
        int carry = 0;

        // choose long input
//        if(n < m) {
//
//        }

        for (int i = n - 1; i > -1; i--) {
            if (a.charAt(i) == '1') carry++;
            if (j > -1 && b.charAt(j--) == '1') carry++;


            if (carry % 2 == 1) res.append('1');
            else res.append('0');

            carry /= 2;
        }

        if (carry == 1) res.append('1');

        res.reverse();

        return res.toString();


    }
}
