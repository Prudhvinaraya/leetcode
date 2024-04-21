class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        // Create an adjacency list representation of the graph
        List<List<Integer>> adjacencyList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjacencyList.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            adjacencyList.get(u).add(v);
            adjacencyList.get(v).add(u); // For bidirectional edges
        }

        // Perform BFS traversal to find if there's a path from source to destination
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n];
        queue.offer(source);
        visited[source] = true;

        while (!queue.isEmpty()) {
            int current = queue.poll();
            if (current == destination) {
                return true; // Path found
            }
            for (int neighbor : adjacencyList.get(current)) {
                if (!visited[neighbor]) {
                    queue.offer(neighbor);
                    visited[neighbor] = true;
                }
            }
        }

        return false; // No path found
    }
}