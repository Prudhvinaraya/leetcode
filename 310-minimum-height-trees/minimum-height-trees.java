import java.util.*;

class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) {
            // If there's only one node, return it as the root
            return Collections.singletonList(0);
        }
        
        // Create an adjacency list to represent the graph
        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            adjList.get(u).add(v);
            adjList.get(v).add(u);
        }
        
        // Initialize a queue for BFS
        Queue<Integer> leaves = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (adjList.get(i).size() == 1) {
                // Add leaves (nodes with only one neighbor) to the queue
                leaves.offer(i);
            }
        }
        
        // Repeat until we have 2 or fewer nodes remaining
        while (n > 2) {
            int leavesSize = leaves.size();
            n -= leavesSize;
            for (int i = 0; i < leavesSize; i++) {
                int leaf = leaves.poll();
                // Remove the leaf node and its edge
                int neighbor = adjList.get(leaf).get(0);
                adjList.get(neighbor).remove((Integer)leaf);
                if (adjList.get(neighbor).size() == 1) {
                    // If the neighbor becomes a leaf after removal, add it to the queue
                    leaves.offer(neighbor);
                }
            }
        }
        
        // The remaining nodes in the queue are the roots of MHTs
        return new ArrayList<>(leaves);
    }
}
