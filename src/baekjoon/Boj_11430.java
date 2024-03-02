package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.*;

public class Boj_11430 {
    private static int n;
    private static int[][] result;
    private static Map<Integer, List<Integer>> graph = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        result = new int[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            List<Integer> list = new ArrayList<>();
            int index = 0;
            while(st.hasMoreTokens()) {
                int token = Integer.parseInt(st.nextToken());
                if (token > 0) {
                    list.add(index);
                }
                index++;
            }
            graph.put(i, list);
        }

        for (int i = 0; i < n; i++) {
            Map<Integer, Boolean> visited = new HashMap<>();
            visited.put(i, true);
            dfs(i, i, visited);
        }

        for (int i = 0; i < result.length; i++) {
            for (int j = 0; j < result[i].length; j++) {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }

    }

    private static void dfs(int start, int current, Map<Integer, Boolean> visited) {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        for (int nextVertex : graph.get(current)) {
            if (result[start][nextVertex] == 0) {
                result[start][nextVertex] = 1;
                dfs(start, nextVertex, visited);
            }
        }
    }
}