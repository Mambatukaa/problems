public class BinarySearch {
    public static boolean binarySearch(int[] arr, int needle) {
        int lo = 0;
        int high = arr.length;

        do {
            int mid = (lo + (high-lo) / 2);
            int v = arr[mid];

            System.out.println(needle + " ");

            if(needle == v) {
                return true;
            } else if(needle < v) {
                high = mid;
            } else {
                lo = mid - 1;
            }
        } while(lo < high);

        return false;
    }


    public static void main(String[] args) {
        boolean response = binarySearch(new int[]{1,2,3,4,5}, 5);

        System.out.println(response);

    }
}
