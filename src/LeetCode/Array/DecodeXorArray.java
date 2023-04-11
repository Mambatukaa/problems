package LeetCode.Array;

// 1720
public class DecodeXorArray {
    final private int[] encoded;
    final private int first;


    public DecodeXorArray(int[] encoded, int first) {
        this.encoded = encoded;
        this.first = first;
    }

    // Time complexity: O(n)
    // Space complexity: O(n)
    public int[] naive() {
        int[] decoded = new int[encoded.length + 1];
        decoded[0] = first;

        for (int i = 0; i < encoded.length; i++) {
            int val = decoded[i] ^ encoded[i];
            decoded[i + 1] = val;
        }

        return decoded;
    }
}
