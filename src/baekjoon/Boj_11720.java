package baekjoon;

import java.util.Scanner;

public class Boj_11720 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int result = 0;
        String s = scanner.next();
        char[] chars = s.toCharArray();

        for (int i = 0; i < chars.length; i++) {
            result += chars[i] - '0';
        }

        System.out.println(result);
    }
}
