package baekjoon;

import java.io.*;
import java.util.Scanner;

public class Boj_1546 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int max = 0;
        int sum = 0;
        for (int i = 0; i < N; i++) {
            int readNum = sc.nextInt();
            if (readNum > max) max = readNum;
            sum += readNum;
        }

        System.out.println(sum / max * 100.0 / N);
    }
}
