public class Main {
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in); // import 없이 직접 경로 지정

        int N = sc.nextInt();
        int min = 1000001;
        int max = -1000001;

        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            if (num < min) {
                min = num;
            }
            if (num > max) {
                max = num;
            }
        }

        System.out.println(min + " " + max);
    }
}
