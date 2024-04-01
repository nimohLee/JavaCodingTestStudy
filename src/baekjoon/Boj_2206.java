package baekjoon;
/**
 * 1. 아이디어
 *  - 행렬 최단 경로이므로 암시적 BFS
 *  - 시작하는 칸, 끝나는 칸 포함
 *  - 벽을 하나 씩 부순 모든 시나리오마다 BFS를 수행
 *  - 최단거리가 가장 작은 BFS의 결과를 반환
 *  - 깊은 복사를 통해 원본과 분리하기
 *  - 연구소 문제와 비슷
 * 2. 자료구조
 *  - 인접행렬(배열)
 *  - 네 방향 배열
 * 3. 시간복잡도
 *  - O((NM)^2) -> 문제의 시간 제한이 2초이기 때문에 넉넉?
 */
import java.util.*;
import java.io.*;
class Boj_2206 {
    private static int[][] map;
    private static int n;
    private static int m;
    private static int[] dr = {0, 1, 0, -1};
    private static int[] dc = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new int[n][m];

        for (int i=0; i<n; i++) {
            String line = br.readLine();
            for (int j=0; j<m; j++) {
                map[i][j] = line.charAt(j) - '0';
            }
        }

        System.out.println(bfs());
    }

    private static int bfs() {
        boolean[][][] visited = new boolean[n][m][2];
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0, 1, 0});
        visited[0][0][0] = true;
        while (!queue.isEmpty()) {
            int[] polled = queue.poll();
            int curRow = polled[0];
            int curCol = polled[1];
            int curLevel = polled[2];
            int isBroken = polled[3];

            if (curRow == n-1 && curCol == m-1) {
                return curLevel;
            }

            for (int i=0; i<4; i++) {
                int nextRow = curRow + dr[i];
                int nextCol = curCol + dc[i];

                if (nextRow < 0 || nextCol < 0 || nextRow >= n || nextCol >= m) {
                    continue;
                }

                if (isBroken == 0) {
                    if (map[nextRow][nextCol] == 1 && !visited[nextRow][nextCol][1]) {
                        queue.offer(new int[]{nextRow, nextCol, curLevel + 1, 1});
                        visited[nextRow][nextCol][1] = true;
                    }
                }

                if (map[nextRow][nextCol] == 1 && visited[nextRow][nextCol][0]) {
                    if (isBroken == 1) {
                        continue;
                    }
                    queue.offer(new int[]{nextRow, nextCol, curLevel + 1, 1});
                } else {
                    queue.offer(new int[]{nextRow, nextCol, curLevel + 1, isBroken});
                    map[nextRow][nextCol] = 1;
                }
            }
        }

        return -1;
    }
}