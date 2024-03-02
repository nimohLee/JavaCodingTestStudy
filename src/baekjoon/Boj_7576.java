package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj_7576 {
    private static int row;
    private static int column;
    private static int[][] box;
    private static int[] dr = {0, 1, 0, -1};
    private static int[] dc = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        column = Integer.parseInt(st.nextToken());
        row = Integer.parseInt(st.nextToken());
        box = new int[row][column];

        // 토마토 박스 세팅
        for (int i = 0; i < row; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < column; j++) {
                box[i][j] = Integer.parseInt(st.nextToken());
            }
        }



        int day = 0;

        while(true) {
            int count = 0;
            boolean[][] visited = new boolean[row][column];
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < column; j++) {
                    if (visited[i][j] || box[i][j] != 1) {
                        continue;
                    }
                    visited[i][j] = true;
                    count += process(i, j, visited);
                }
            }
            day++;

            if (isAllDone()) {
                break;
            }
            if (count == 0) {
                day = -1;
                break;
            }
        }

        System.out.println(day);

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

    private static int process(int curRow, int curColumn, boolean[][] visited) {
        int count = 0;
        for (int i = 0; i < 4; i++) {
            int nextRow = curRow + dr[i];
            int nextColumn = curColumn + dc[i];
            if (nextRow < 0 || nextColumn <0 || nextRow >= row || nextColumn >= column) {
                continue;
            }
            if (visited[nextRow][nextColumn]) {
                continue;
            }
            if (box[nextRow][nextColumn] == 0) {
                count++;
                box[nextRow][nextColumn] = 1;
                visited[nextRow][nextColumn] = true;
            }
        }

        return count;
    }
}
