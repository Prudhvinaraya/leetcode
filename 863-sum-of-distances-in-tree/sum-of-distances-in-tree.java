import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] sumOfDistancesInTree(int n, int[][] edges) {
        // Initialize adjacency list representation of the tree
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        
        // Initialize arrays to store subtree sizes and sum of distances
        int[] subtreeSizes = new int[n];
        int[] totalDistances = new int[n];
        
        // First DFS to calculate subtree sizes
        dfs1(0, -1, graph, subtreeSizes, totalDistances);
        
        // Second DFS to calculate sum of distances for each node
        dfs2(0, -1, graph, subtreeSizes, totalDistances, n);
        
        return totalDistances;
    }
    
    private void dfs1(int node, int parent, List<List<Integer>> graph, int[] subtreeSizes, int[] totalDistances) {
        subtreeSizes[node] = 1;
        for (int neighbor : graph.get(node)) {
            if (neighbor != parent) {
                dfs1(neighbor, node, graph, subtreeSizes, totalDistances);
                subtreeSizes[node] += subtreeSizes[neighbor];
                totalDistances[node] += totalDistances[neighbor] + subtreeSizes[neighbor];
            }
        }
    }
    
    private void dfs2(int node, int parent, List<List<Integer>> graph, int[] subtreeSizes, int[] totalDistances, int n) {
        for (int neighbor : graph.get(node)) {
            if (neighbor != parent) {
                // Formula for sum of distances:
                // dist[node] = dist[parent] - subtreeSizes[neighbor] + (n - subtreeSizes[neighbor])
                totalDistances[neighbor] = totalDistances[node] - subtreeSizes[neighbor] + (n - subtreeSizes[neighbor]);
                dfs2(neighbor, node, graph, subtreeSizes, totalDistances, n);
            }
        }
    }
}
