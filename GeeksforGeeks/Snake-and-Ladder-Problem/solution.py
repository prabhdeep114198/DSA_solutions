import java.util.*;

class Solution {
    public int minThrows(int n, int[] lad, int[] sn) {

        int total = n * n;

        int[] move = new int[total + 1];
        Arrays.fill(move, -1);

        // Store ladders
        for (int i = 0; i < lad.length; i += 2) {
            move[lad[i]] = lad[i + 1];
        }

        // Store snakes
        for (int i = 0; i < sn.length; i += 2) {
            move[sn[i]] = sn[i + 1];
        }

        boolean[] visited = new boolean[total + 1];

        // {position, throws}
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{1, 0});
        visited[1] = true;

        while (!q.isEmpty()) {

            int[] curr = q.poll();

            int pos = curr[0];
            int throwsCount = curr[1];

            if (pos == total) {
                return throwsCount;
            }

            // Try dice values 1 to 6
            for (int dice = 1; dice <= 6; dice++) {

                int next = pos + dice;

                if (next > total) {
                    continue;
                }

                // Snake or ladder
                if (move[next] != -1) {
                    next = move[next];
                }

                if (!visited[next]) {
                    visited[next] = true;
                    q.add(new int[]{next, throwsCount + 1});
                }
            }
        }

        return -1;
    }
}