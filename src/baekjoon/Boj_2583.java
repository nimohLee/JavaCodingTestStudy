package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Boj_2583 {
    private static int M;
    private static int N;
    private static int[][] map;
    private static int[] dr = {0, -1, 0, 1};
    private static int[] dc = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        map = new int[M][N];

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            for (int y=y1; y<y2; y++) {
                for (int x=x1; x<x2; x++) {
                    map[y][x] = 1;
                }
            }
        }

        List<Integer> countList = new ArrayList<>();
        int areaCount = 0;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == 0) {
                    countList.add(bfs(i, j));
                    areaCount++;
                }
            }
        }

        System.out.println(areaCount);
        countList.stream().sorted().forEach((item)->{
            System.out.print(item + " ");
        });
    }

    private static int bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        int count = 1;
        queue.offer(new int[]{x, y});
        map[x][y] = 1;
        while (!queue.isEmpty()) {
            int[] polled = queue.poll();
            int curRow = polled[0];
            int curCol = polled[1];

            for (int i = 0; i < 4; i++) {
                int nextRow = curRow + dr[i];
                int nextCol = curCol + dc[i];
                if (valid(nextRow, nextCol)) {
                    queue.offer(new int[]{nextRow, nextCol});
                    map[nextRow][nextCol] = 1;
                    count++;
                }
            }
        }

        return count;
    }

    private static boolean valid(int nextRow, int nextCol) {
        if (nextRow < 0 || nextCol < 0 || nextRow >= M || nextCol >= N) {
            return false;
        }

        return map[nextRow][nextCol] == 0;
    }
}
