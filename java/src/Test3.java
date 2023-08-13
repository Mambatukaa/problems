import java.security.spec.RSAOtherPrimeInfo;
import java.util.Arrays;
import java.util.Scanner;

public class Test3 {

    public static void main(String[] args) {
        char[] array = {'a', 'b', 'c'};
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter a starting point: ");
        int start = scanner.nextInt();

        System.out.println("Enter a length: ");
        int len = scanner.nextInt();

        char[] response = response(array, start, len);

        System.out.println(Arrays.toString(response));
    }

    static char[] response(char[] array, int start, int len) {
        if (start < 0 || len < 0 || start + len > array.length) {
            return null;
        }

        char[] updatedArr = new char[len];

        for(int i = start, j=0; j < len; i++, j++){
            updatedArr[j] = array[i];
        }

        return updatedArr;
    }
}
