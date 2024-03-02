package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Boj_14502 {
    private static int row;
    private static int column;
    private static int[][] map;
    private static int[][] copyMap;
    private static List<int[]> virusLocation = new ArrayList<>();
    private static int[] dr = {0, 1, 0, -1};
    private static int[] dc = {1, 0, -1, 0};
    private static int safeAreaCount = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        row = Integer.parseInt(st.nextToken());
        column = Integer.parseInt(st.nextToken());
        map = new int[row][column];

        for (int i = 0; i < row; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < column; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 2) {
                    virusLocation.add(new int[]{i, j});
                }
            }
        }

        dfs(0);
        System.out.println(safeAreaCount);
    }

    private static void dfs(int wallCount) {
        if (wallCount == 3) {
            safeAreaCount = Math.max(bfs(), safeAreaCount);
        } else {
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < column; j++) {
                    if (map[i][j] == 0) {
                        map[i][j] = 1;
                        dfs(wallCount+1);
                        map[i][j] = 0;
                    }
                }
            }
        }
    }

    private static int bfs() {
        boolean[][] visited = new boolean[row][column];
        Queue<int[]> queue = new LinkedList<>();
        for (int[] virus : virusLocation) {
            queue.offer(virus);
        }
        copyMap = new int[row][column];

//        for (int i=0; i<map.length; i++) {
//            copyMap[i] = map[i].clone();
//        }

        copyMap = map.clone();

        while (!queue.isEmpty()) {
            int[] polled = queue.poll();
            int curRow = polled[0];
            int curCol = polled[1];

            for (int i=0; i<4; i++) {
                int nextRow = curRow + dr[i];
                int nextCol = curCol + dc[i];

                if (nextRow < 0 || nextCol < 0 || nextRow >= row || nextCol >= column) {
                    continue;
                }

                if (!visited[nextRow][nextCol] && copyMap[nextRow][nextCol] == 0) {
                    queue.offer(new int[]{nextRow, nextCol});
                    copyMap[nextRow][nextCol] = 2;
                    visited[nextRow][nextCol] = true;
                }
            }
        }
        return countSafeArea(copyMap);
    }

    private static int countSafeArea(int[][] map) {
        int result = 0;
        for (int i = 0;i < row; i++) {
            for (int j = 0;j < column; j++) {
                if (map[i][j] == 0) {
                    result++;
                }
            }
        }

        return result;
    }
}
