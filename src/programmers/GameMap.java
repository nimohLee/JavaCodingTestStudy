package programmers;

import java.util.LinkedList;
import java.util.Queue;

public class GameMap {

    private boolean[][] visited;
    private int[] dr = {0, 1, 0, -1};
    private int[] dc = {1, 0, -1, 0};
    private int rowLength;
    private int colLength;
    private int[][] maps;
    private int count = 0;

    private boolean isValid(int row, int column) {
        if (row >= 0 && row < rowLength && column >= 0 && column < colLength && maps[row][column] != 0) {
            return true;
        }
        return false;
    }

    public int solution(int[][] maps) {
        rowLength = maps.length;
        colLength = maps[0].length;
        visited = new boolean[rowLength][colLength];
        this.maps = maps;

        return bfs(0, 0);
    }

    private int bfs(int row, int column) {
        Queue<int[]> queue = new LinkedList<>();

        queue.offer(new int[]{row, column, 1});
        visited[row][column] = true;

        while (!queue.isEmpty()) {

            int[] current = queue.poll();
            int currentRow = current[0];
            int currentCol = current[1];
            int currentCount = current[2];

            if (currentRow == rowLength - 1 && currentCol == colLength - 1) {
                return currentCount;
            }

            for (int i = 0; i < 4; i++) {
                int nextRow = currentRow + dr[i];
                int nextCol = currentCol + dc[i];

                if (isValid(nextRow, nextCol)) {
                    if (!visited[nextRow][nextCol]) {
                        visited[nextRow][nextCol] = true;
                        queue.offer(new int[]{nextRow, nextCol, ++currentCount});
                    }
                }
            }
        }
        return -1;
    }
}


