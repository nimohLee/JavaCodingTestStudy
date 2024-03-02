package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Boj_12865 {

        private static int N;
        private static int K;
        private static Map<Set<Item>, Integer> memo = new HashMap<>();
        private static List<Item> items = new ArrayList<>();

        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            for (int i = 0; i < N; i++) {
                StringTokenizer loopSt = new StringTokenizer(br.readLine());
                int weight = Integer.parseInt(loopSt.nextToken());
                int value = Integer.parseInt(loopSt.nextToken());
                Item item = new Item(weight, value);
                items.add(item);
            }

            for (Item item : items) {
                Set<Item> itemSet = new HashSet<>();
                itemSet.add(item);

            }
            int result = Integer.MIN_VALUE;
            for (int i = 0; i < N; i++) {
                Set<Item> itemSet = new HashSet<>();
                Item item = items.get(i);
                itemSet.add(item);
                result = Math.max(result, dfs(itemSet, item.getValue()));
            }

            System.out.println(result);
        }

        private static int dfs(Set<Item> itemSet, int valueSum) {

            valueSum = getValueSum(itemSet);

            for (Item item : items) {
                if (!itemSet.contains(item)) {
                    if (!validate(itemSet, item)) {
                        continue;
                    }
                    itemSet.add(item);
                    if (memo.containsKey(itemSet)) {
                        valueSum = Math.max(memo.get(itemSet), valueSum);
                    } else {
                        int result = dfs(itemSet, valueSum);
                        if (result > valueSum) {
                            memo.put(itemSet, result);
                            valueSum = Math.max(result, valueSum);
                        }
                    }

                }
            }

            return valueSum;
        }

        private static boolean validate(Set<Item> itemSet, Item item) {
            return K >= itemSet.stream()
                    .mapToInt(Item::getWeight)
                    .sum() + item.getWeight();
        }

        private static int getValueSum(Set<Item> itemSet) {
            return itemSet.stream()
                    .mapToInt(Item::getValue)
                    .sum();
        }

        private static class Item {
            private int weight;
            private int value;

            public Item(int weight, int value) {
                this.weight = weight;
                this.value = value;
            }

            public int getValue() {
                return value;
            }

            public int getWeight() {
                return weight;
            }

            @Override
            public boolean equals(Object o) {
                if (this == o) return true;
                if (o == null || getClass() != o.getClass()) return false;
                Item item = (Item) o;
                return weight == item.weight && weight == item.value;
            }

            @Override
            public int hashCode() {
                return Objects.hash(weight, value);
            }
        }
}
