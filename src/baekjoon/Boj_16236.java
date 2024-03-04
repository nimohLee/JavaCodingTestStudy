package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Boj_16236 {
    private static int[][] map;
    private static int N;
    private static int dr[] = {0, 1, 0, -1};
    private static int dc[] = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        map = new int[N][N];

        Shark shark = null;
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int token = Integer.parseInt(st.nextToken());

                if (token == 9) {
                   shark = new Shark(i, j);
                   map[i][j] = 0;
                }

                map[i][j] = token;
            }
        }

        dfs(shark);

        shark.printDay();
    }

    private static void dfs(Shark shark) {

        int currentX = shark.getX();
        int currentY = shark.getY();

        if (shark.isBiggerThan(map[currentX][currentY])) {
            shark.eat();
            map[currentX][currentY] = 0;
        }

        if (shark.isCantEatMore()) {
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nextX = currentX + dr[i];
            int nextY = currentY + dc[i];

            if (nextX >= N || nextY >= N || nextX < 0 || nextY < 0) {
                continue;
            }

            if (shark.isSmallerThan(map[nextX][nextY])) {
                continue;
            }

            dfs(shark.move(nextX, nextY));
        }

    }

    private static class Shark {
        private int x;
        private int y;
        private int size = 2;
        private int eatCount = 0;
        private int day = 0;

        private Shark(){}

        public Shark(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public Shark move(int x, int y) {
            this.x = x;
            this.y = y;
            day++;

            return this;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public boolean isSmallerThan(int size) {
            return this.size < size;
        }

        public boolean isBiggerThan(int size) {
            return this.size > size;
        }

        public void eat() {
            eatCount++;
            if (size == eatCount) {
                size++;
                eatCount = 0;
            }
        }

        public boolean isCantEatMore() {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (map[i][j] > 0 && map[i][j] < size) {
                        return false;
                    }
                }
            }
            return true;
        }

        public void printDay() {
            System.out.println(day);
        }

    }
}
