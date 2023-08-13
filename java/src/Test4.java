import java.util.Scanner;

public class Test4 {

    static int intReverse(int num) {
        int sign = 1;

        if(num == 0) return 0;
        if(num < 0) {
            sign = -1;
            num = -num;
        }

        int reverse = 0;

        while(num != 0) {
            reverse = (reverse * 10) + (num % 10);
            num /= 10;
        }

        return reverse;
    }

    public static void main(String[] args) {
        System.out.println("Enter an integer number: ");
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();

        System.out.println(intReverse(num));
    }
}
