public class Test2 {

    public static void main(String[] args) {
        int[] arr = {1,2,3,4};

        System.out.println(sub(arr));
    }

    static int sub(int[] array) {
        int sumOdd = 0;
        int sumEven = 0;

        for(int el: array) {
            if(el % 2 == 0) {
                sumEven += el;
            } else {
                sumOdd += el;
            }
        }

        return sumOdd - sumEven;

    };
}
