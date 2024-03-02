package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Boj_7576_retry {
    private static int row;
    private static int column;
    private static int[][] box;
    private static int[] dr = {0, 1, 0, -1};
    private static int[] dc = {1, 0, -1, 0};
    private static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        column = Integer.parseInt(st.nextToken());
        row = Integer.parseInt(st.nextToken());
        box = new int[row][column];
        visited = new boolean[row][column];
        // 토마토 박스 세팅
        for (int i = 0; i < row; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < column; j++) {
                box[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int day = bfs();

        if (!isAllDone()) {
            day = -1;
        }

        System.out.println(day);

    }

    private static int bfs() {
        Queue<Integer[]> queue = new LinkedList<>();

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                if (box[i][j] == 1) {
                    queue.offer(new Integer[]{i, j, 0});
                }
            }
        }

        if (queue.size() == 0) {
            return -1;
        }

        Integer[] peeked = queue.peek();
        int firstRow = peeked[0];
        int firstCol = peeked[1];

        visited[firstRow][firstCol] = true;

        int maxDay = 0;

        while (!queue.isEmpty()) {
            Integer[] polled = queue.poll();
            int curRow = polled[0];
            int curCol = polled[1];
            int day = polled[2];

            for (int i = 0; i < 4; i++) {
                int nextRow = curRow + dr[i];
                int nextCol = curCol + dc[i];
                if (nextRow < 0 || nextCol < 0 || nextRow >= row || nextCol >= column) {
                    continue;
                }
                if (box[nextRow][nextCol] == 0 && !visited[nextRow][nextCol]) {
                    visited[nextRow][nextCol] = true;
                    box[nextRow][nextCol] = 1;
                    queue.offer(new Integer[]{nextRow, nextCol, day+1});
                    maxDay = day+1;
                }
            }
        }

        return maxDay;

    }

    private static boolean isAllDone() {
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                if (box[i][j] == 0) {
                    return false;
                }
            }
        }
        return true;
    }
}
