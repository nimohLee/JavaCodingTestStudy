package baekjoon;

import java.util.*;
import java.io.*;
import java.util.stream.*;

class Boj_1260 {

    private static Map<Integer, List<Integer>> map = new HashMap<>();
    private static List<Integer> dfsVisited = new ArrayList<>();
    private static List<Integer> bfsVisited = new ArrayList<>();
    private static int n;
    private static int m;
    private static int v;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= n; i++) {
            map.put(i, new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int startV = Integer.parseInt(st.nextToken());
            int endV = Integer.parseInt(st.nextToken());
            addVertexAndSort(startV, endV);
            addVertexAndSort(endV, startV);
        }
        dfsVisited.add(v);
        dfs(v);
        bfs(v);

        System.out.println(
                dfsVisited.stream()
                        .map(String::valueOf)
                        .collect(Collectors.joining(" "))
        );

        System.out.println(
                bfsVisited.stream()
                        .map(String::valueOf)
                        .collect(Collectors.joining(" "))
        );
    }

    private static void addVertexAndSort(int startV, int endV) {
        List<Integer> vertexs = map.get(startV);
        vertexs.add(endV);
        Collections.sort(vertexs);
    }

    private static void dfs(int currentV) {
        for (Integer vertex : map.get(currentV)) {
            if (!dfsVisited.contains(vertex)) {
                dfsVisited.add(vertex);
                dfs(vertex);
            }
        }
    }

    private static void bfs(int startV) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(startV);
        bfsVisited.add(startV);
        while (!queue.isEmpty()) {
            int curV = queue.poll();
            for (Integer nextV : map.get(curV)) {
                if (!bfsVisited.contains(nextV)) {
                    queue.offer(nextV);
                    bfsVisited.add(nextV);
                }
            }
        }
    }
}
