class Solution {
    public boolean isCycle(int V, int[][] edges) {

        // Build adjacency list
        ArrayList<ArrayList<Integer>> al = new ArrayList<>();

        for (int i = 0; i < V; i++) {
            al.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];

            al.get(u).add(v);
            al.get(v).add(u);
        }

        boolean[] visited = new boolean[V];
        Queue<int[]> q = new LinkedList<>();

        for (int i = 0; i < V; i++) {

            if (visited[i]) {
                continue;
            }

            q.add(new int[]{i, -1});
            visited[i] = true;

            while (!q.isEmpty()) {
                int[] current = q.poll();

                int node = current[0];
                int parent = current[1];

                for (int neighbour : al.get(node)) {

                    if (!visited[neighbour]) {
                        visited[neighbour] = true;
                        q.add(new int[]{neighbour, node});
                    }
                    else if (neighbour != parent) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
}