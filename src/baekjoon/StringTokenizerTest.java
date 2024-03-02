package baekjoon;

import java.io.*;
import java.util.StringTokenizer;

public class StringTokenizerTest {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        String sInput = br.readLine();
//
//        StringTokenizer stringTokenizer = new StringTokenizer(sInput);
//        while (stringTokenizer.hasMoreTokens()) {
//            System.out.println(stringTokenizer.nextToken());
//        }
//        int iInput = br.read();
//        stringTokenizer = new StringTokenizer(Integer.toString(iInput));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s = br.readLine();
        StringTokenizer stringTokenizer = new StringTokenizer(s);
        while (stringTokenizer.hasMoreTokens()) {
            bw.write(stringTokenizer.nextToken() + "\n");
        }
        bw.close();
//
//        StringBuilder stringBuilder = new StringBuilder();
//        stringBuilder.append(3);
//        stringBuilder.append("hi");
//        stringBuilder.append(true);
//
//        stringBuilder.insert(1, "hello");

//        System.out.println(stringBuilder.toString());
    }
}
