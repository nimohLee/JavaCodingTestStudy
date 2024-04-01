package baekjoon;

import java.util.*;
import java.io.*;
/**
 * 1. 아이디어 : 최소 칸 수! 이므로 BFS 알고리즘 사용
 * 네 방향 순회를 사용하며 방문한 곳은 그래프 자체를 0으로 수정
 * 2. 자료구조 : 인접배열로 미로 구현
 * 3. 시간복잡도 : n^2
 */
class Boj_2178 {
    private static int[][] maze;
    private static int[] dr = {0, 1, 0, -1};
    private static int[] dc = {1, 0, -1, 0};
    private static int n;
    private static int m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        maze = new int[n][m];

        for (int i = 0;i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                maze[i][j] = line.charAt(j) - '0';
            }
        }

        System.out.println(bfs());
    }

    private static int bfs() {
        int startLevel = 1;
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0, startLevel});
        while (!queue.isEmpty()) {
            int[] polled = queue.poll();
            int curRow = polled[0];
            int curCol = polled[1];
            int curLevel = polled[2];

            if(curRow == (n-1) && curCol == (m-1)) {
                return curLevel;
            }

            for (int i=0; i<4; i++) {
                int nextRow = curRow + dr[i];
                int nextCol = curCol + dc[i];

                if (nextRow < 0 || nextCol < 0 || nextRow >= n || nextCol >= m) {
                    continue;
                }

                if (maze[nextRow][nextCol] == 1) {
                    queue.offer(new int[]{nextRow, nextCol, curLevel + 1});
                    maze[nextRow][nextCol] = 0;
                }
            }
        }
        return startLevel;
    }
}